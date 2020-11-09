import json
from pprint import pprint
from datetime import datetime, timedelta

from parse_functions import *
from write_to_mysql import *

inbound_audio_functions = [get_inbound_audio_packets_received_per_second, get_inbound_audio_bytes_received_per_second,
                           get_inbound_audio_packets_lost, get_inbound_audio_jitter,
                           get_inbound_audio_jitter_buffer_delay,
                           get_inbound_audio_total_samples_received, get_inbound_audio_level, get_inbound_audio_energy,
                           ]  # removed inbound_audio_round_trip_time - does not exist in inbound only connection?

inbound_video_functions = [get_inbound_video_packets_received_per_second, get_inbound_video_bytes_received_per_second,
                           get_inbound_video_packets_lost, get_inbound_video_frames_received,
                           get_inbound_video_frames_decoded,
                           get_inbound_video_frames_decoded_per_second, get_inbound_video_frames_dropped,
                           get_inbound_video_frame_width, get_inbound_video_frame_height, get_inbound_video_frames_per_second
                           ]  # removed inbound_video_round_trip_time - does not exist in inbound only connection?

outbound_audio_functions = [get_outbound_audio_packets_sent_per_second, get_outbound_audio_bytes_sent_per_second]
outbound_video_functions = [get_outbound_video_packets_sent_per_second, get_outbound_video_bytes_sent_per_second,
                            get_outbound_video_frames_encoded, get_outbound_video_frames_encoded_per_second,
                            get_outbound_video_frames_sent, get_outbound_video_quality_limitation_reason,
                            get_outbound_video_quality_limitation_resolution_change, get_outbound_video_frame_width,
                            get_outbound_video_frame_height, get_outbound_video_frames_per_second]


def iterate_through_functions(stat_data):
    array = dict()
    for funct in [*inbound_audio_functions, *inbound_video_functions]:
        new_stat_title, new_stat_content = funct(stat_data)
        new_stat_data = create_timestamped_stat_data(new_stat_title, new_stat_content)
        array = merge_stats(array, new_stat_data)
    return array


def merge_stats(array, stat_data):
    stat_data = convert_stat_data_to_dict(stat_data)

    for timestamp in stat_data.keys():
        if timestamp not in array.keys():
            array[timestamp] = stat_data[timestamp]
        else:
            array[timestamp] = {**array[timestamp], **stat_data[timestamp]}
    return array


def convert_stat_data_to_dict(stat_data):
    output = dict()
    for stat_value in stat_data:
        output[next(iter(stat_value))] = stat_value[next(iter(stat_value))]
    return output


def create_timestamped_stat_data(new_stat_title, new_stat_content):
    timestamped_stat_data = get_timestamp_list(new_stat_content)
    for _ in new_stat_content.values():
        v_list = _['values'][1:-1]
        v_list = [round(float(_)) for _ in v_list.split(',')]
    for _ in timestamped_stat_data:
        position = timestamped_stat_data.index(_)
        timestamped_data = timestamped_stat_data[position]
        timestamped_key = next(iter(timestamped_data))
        timestamped_value = timestamped_data[timestamped_key]
        timestamped_value[new_stat_title] = v_list[position]
    return timestamped_stat_data


def get_timestamp_list(new_stat_content):
    stat_values = new_stat_content[next(iter(new_stat_content))]
    start_time = datetime.strptime(stat_values['startTime'][:-5], '%Y-%m-%dT%H:%M:%S')
    end_time = datetime.strptime(stat_values['endTime'][:-5], '%Y-%m-%dT%H:%M:%S')
    ticks = (end_time - start_time).seconds
    timestamp_list = list()
    event_time = start_time
    for _ in range(ticks):
        timestamp_list.append({event_time.strftime("%Y-%m-%d %H:%M:%S"): {}})
        event_time += timedelta(seconds=1)
    return timestamp_list


def find_interview_id(url):
    start = 'interviews/'
    end = '/online'
    return url[url.find(start)+len(start):url.rfind(end)]


if __name__ == '__main__':
    with open('webrtc_internals_dump_reconnected.txt') as raw_stats:
        all_data = json.load(raw_stats)

    for peer_connection_id, peer_connection_data in all_data['PeerConnections'].items():
        print('\npeer connection id:', peer_connection_id)
        stat_data = peer_connection_data['stats']
        stats_parsed = iterate_through_functions(stat_data)
        interview_url = peer_connection_data['url']
        interview_id = find_interview_id(interview_url)
        add_stats_row_to_database(stats_parsed, interview_id, peer_connection_id)
