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


def get_timestamp_list(stats):
    for _ in stats.values():
        start_time = datetime.strptime(_['startTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        end_time = datetime.strptime(_['endTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
    ticks = (end_time - start_time).seconds
    timestamp_list = list()
    event_time = start_time
    for _ in range(ticks):
        timestamp_list.append({event_time: {}})
        event_time += timedelta(seconds=1)

    return timestamp_list


def add_stats_to_list(stats_list, new_stat, new_stat_title):
    for _ in new_stat.values():
        v_list = _['values'][1:-1]
        v_list = [round(float(_)) for _ in v_list.split(',')]
    for _ in stats_list:
        position = stats_list.index(_)
        timestamped_data = stats_list[position]
        timestamped_key = next(iter(timestamped_data))
        timestamped_value = timestamped_data[timestamped_key]
        timestamped_value[new_stat_title] = v_list[position]
    return (stats_list)


def iterate_through_functions(stat_data):
    _, stats = get_inbound_audio_bytes_received_per_second(stat_data)
    stats_list = get_timestamp_list(stats)
    for funct in inbound_audio_functions:
        new_stat_title, new_stat = funct(stat_data)
        add_stats_to_list(stats_list, new_stat, new_stat_title)
    for funct in inbound_video_functions:
        new_stat_title, new_stat = funct(stat_data)
        add_stats_to_list(stats_list, new_stat, new_stat_title)
    return stats_list


if __name__ == '__main__':
    with open('webrtc_internals_dump_3.txt') as raw_stats:
        all_data = json.load(raw_stats)

    stat_data = all_data['PeerConnections']['55942-1']['stats']

    stats_parsed = iterate_through_functions(stat_data)

    add_stats_row_to_database(stats_parsed)
