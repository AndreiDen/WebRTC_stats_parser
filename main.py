import json
from pprint import pprint
from datetime import datetime, timedelta

from stats_list import *
from write_to_mysql import *


def parse_file_stats(stats_data):
    array = dict()
    for key in list(stats_data.keys()):  # detecting connection type
        if key.startswith('RTCOutboundRTPAudioStream') and key.endswith('headerBytesSent'):
            peer_connection_type = 'outbound'
            keys_dict = {'RTCOutboundRTPAudioStream': parsed_stat_list['RTCOutboundRTPAudioStream'],
                             'RTCOutboundRTPVideoStream': parsed_stat_list['RTCOutboundRTPVideoStream']}
            break
        else:
            peer_connection_type = 'inbound'
            keys_dict = {'RTCInboundRTPAudioStream': parsed_stat_list['RTCInboundRTPAudioStream'],
                             'RTCInboundRTPVideoStream': parsed_stat_list['RTCInboundRTPVideoStream']}

    for stream, stats in keys_dict.items():  # getting stats relevant to the connectin type
        for stat in stats:
            to_remove = ['RTC', 'RTP', 'Stream']
            stream_title = stream
            for _ in to_remove:
                stream_title = stream_title.replace(_, '')
            new_stat_title = ''.join(stream_title.split()) + '_' + stat
            for key, value in stats_data.items():
                if key.startswith(stream) and key.endswith(stat):
                    new_stat_content = ({key: value})
                    new_stat_data = create_timestamped_stat_data(new_stat_title, new_stat_content)
                    array = merge_stats(array, new_stat_data)
    return peer_connection_type, array


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
    return url[url.find(start) + len(start):url.rfind(end)]


def iterate_through_peer_connections(all_data):
    parsed_peer_connections_data = dict()
    for peer_connection_id, peer_connection_data in all_data['PeerConnections'].items():
        interview_id = find_interview_id(peer_connection_data['url'])
        stat_data = peer_connection_data['stats']
        peer_connection_type, stats_parsed = parse_file_stats(stat_data)
        parsed_peer_connections_data[peer_connection_id] = {'interview_id': interview_id,
                                                            'connection_type': peer_connection_type,
                                                            'parsed_stats': stats_parsed}

    return parsed_peer_connections_data


def define_connection_type(stats_parsed):
    if 'OutboundAudio_[bytesSent_in_bits/s]' in list(stats_parsed.values())[5]:  # checks connection type on 5th second
        return 'outbound'
    else:
        return 'inbound'


if __name__ == '__main__':
    print('\n\n')
    with open('webrtc_respondent_moder_1.txt') as raw_stats:
        all_data = json.load(raw_stats)
        parsed_peer_connections_data = iterate_through_peer_connections(all_data)
        pprint(parsed_peer_connections_data)

        add_stats_row_to_database(parsed_peer_connections_data)
