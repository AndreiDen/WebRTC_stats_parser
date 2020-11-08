import json
from pprint import pprint
from stats_list import *
from parse_functions import *
from datetime import datetime, timedelta


def get_timestamp_list(inbound_audio_packets_received_per_second_stats):
    for _ in inbound_audio_packets_received_per_second_stats.values():
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
    return(stats_list)




if __name__ == '__main__':
    with open('webrtc_internals_dump_inbound_only.txt') as raw_stats:
        all_data = json.load(raw_stats)

    # stats_list = list()

    title1, inbound_audio_packets_received_per_second_stats = get_inbound_audio_packets_received_per_second(all_data['PeerConnections']['48752-1']['stats'])
    title2, inbound_audio_bytes_received_per_second_stats = get_inbound_audio_bytes_received_per_second(all_data['PeerConnections']['48752-1']['stats'])
    # _ ,inbound_audio_packets_lost = get_inbound_audio_packets_lost(all_data['PeerConnections']['48752-1']['stats'])[0]
    # _ ,inbound_audio_jitter = get_inbound_audio_jitter(all_data['PeerConnections']['48752-1']['stats'])[0]
    # _ ,inbound_audio_jitter_buffer_delay = get_inbound_audio_jitter_buffer_delay(all_data['PeerConnections']['48752-1']['stats'])[0]
    # _ ,inbound_audio_total_samples_received = get_inbound_audio_total_samples_received(all_data['PeerConnections']['48752-1']['stats'])[0]
    # _ ,inbound_audio_level = get_inbound_audio_level(all_data['PeerConnections']['48752-1']['stats'])[0]
    # _ ,inbound_audio_energy = get_inbound_audio_energy(all_data['PeerConnections']['48752-1']['stats'])[0]
    # _ ,inbound_audio_round_trip_time = get_inbound_audio_round_trip_time(all_data['PeerConnections']['48752-1']['stats'])[0]

    stats_list = get_timestamp_list(inbound_audio_packets_received_per_second_stats)


    list1 = add_stats_to_list(stats_list, inbound_audio_packets_received_per_second_stats, title1)
    list2 = add_stats_to_list(stats_list, inbound_audio_bytes_received_per_second_stats, title2)

    pprint(list2)

inbound_audio_functions = [get_inbound_audio_packets_received_per_second, get_inbound_audio_bytes_received_per_second,
                           get_inbound_audio_packets_lost, get_inbound_audio_jitter, get_inbound_audio_jitter_buffer_delay,
                           get_inbound_audio_total_samples_received, get_inbound_audio_level, get_inbound_audio_energy,
                           get_inbound_audio_round_trip_time]

inbound_video_functions = [get_inbound_video_packets_received_per_second, get_inbound_video_bytes_received_per_second,
                           get_inbound_video_packets_lost, get_inbound_video_frames_received, get_inbound_video_frames_decoded,
                           get_inbound_video_frames_decoded_per_second, get_inbound_video_frames_dropped, get_inbound_video_jitter,
                           get_inbound_video_round_trip_time]
outbound_audio_functions = [get_outbound_audio_packets_sent_per_second, get_outbound_audio_bytes_sent_per_second]
outbound_video_functions = []









