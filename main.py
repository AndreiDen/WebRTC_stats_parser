import json
from pprint import pprint
from stats_list import *
from parse_functions import *
import time
from datetime import datetime, timedelta
from collections import OrderedDict


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


def parse_numeric_stats(stats, stats_title, timestamp_list):
    for _ in stats.values():
        v_list = _['values'][1:-1]
        v_list = [round(float(_)) for _ in v_list.split(',')]
    for _ in timestamp_list:
        position = timestamp_list.index(_)
        timestamped_data = timestamp_list[position]
        timestamped_key = next(iter(timestamped_data))
        timestamped_value = timestamped_data[timestamped_key]
        timestamped_value[stats_title] = v_list[position]

    return(timestamp_list)





if __name__ == '__main__':
    with open('webrtc_internals_dump_inbound_only.txt') as raw_stats:
        all_data = json.load(raw_stats)

    stats_dict = {}

    inbound_audio_packets_received_per_second_stats = get_inbound_audio_packets_received_per_second(all_data['PeerConnections']['48752-1']['stats'])[0]
    inbound_audio_bytes_received_per_second_stats = get_inbound_audio_bytes_received_per_second(all_data['PeerConnections']['48752-1']['stats'])[0]

    empty_timestamp_list = get_timestamp_list(inbound_audio_packets_received_per_second_stats)


    list1 = parse_numeric_stats(inbound_audio_packets_received_per_second_stats, 'inbound_audio_packets_received_per_second_stats', empty_timestamp_list)
    list2 = parse_numeric_stats(inbound_audio_bytes_received_per_second_stats, 'inbound_audio_bytes_received_per_second_stats', list1)

    pprint(list2)










