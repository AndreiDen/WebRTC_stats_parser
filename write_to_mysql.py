import mysql.connector
from datetime import datetime
from pprint import pprint


def r(key):
    if key in stats_array.keys():
        return f"'{stats_array[key]}'"
    else:
        return """'None'"""


def add_stats_row_to_database(stats_parsed, interview_id, peer_connection_id):
    global stats_array
    interview_status = 'past'
    user_name = 'Bob Ross'
    peer_connection_type = 'inbound'

    db = mysql.connector.connect(host='10.1.10.106',
                                 port=3306,
                                 user='admin',
                                 password='admin',
                                 database='webrtcStatsTest')
    cursor = db.cursor()
    for date_time_stamp in stats_parsed.keys():
        stats_array = stats_parsed[date_time_stamp]
        add_stat = ("INSERT IGNORE INTO test2 (interview, interviewStatus, userName, dateTimeStamp, peerConnection, peerConnectionType, inbound_audio_packets_received_per_second, inbound_audio_bytes_received_per_second, inbound_audio_packets_lost, "
                    "inbound_audio_jitter, inbound_audio_jitter_buffer_delay, inbound_audio_total_samples_received, inbound_audio_level, inbound_audio_energy,"
                    "inbound_video_packets_received_per_second, inbound_video_bytes_received_per_second, "
                    "inbound_video_packets_lost, "
                    "inbound_video_frame_width, inbound_video_frame_height, inbound_video_frames_per_second, "
                    "inbound_video_frames_decoded, inbound_video_frames_decoded_per_second, "
                    "inbound_video_frames_received, inbound_video_frames_dropped) "
                    f"VALUES ('{interview_id}', '{interview_status}', '{user_name}', '{date_time_stamp}', '{peer_connection_id}', '{peer_connection_type}', "
                    f"{r('inbound_audio_packets_received_per_second')}, {r('inbound_audio_bytes_received_per_second')}, {r('inbound_audio_packets_lost')}, "
                    f"{r('inbound_audio_jitter')}, {r('inbound_audio_jitter_buffer_delay')}, {r('inbound_audio_total_samples_received')}, "
                    f"{r('inbound_audio_level')}, {r('inbound_audio_energy')},"
                    f"{r('inbound_video_packets_received_per_second')}, {r('inbound_video_bytes_received_per_second')}, "
                    f"{r('inbound_video_packets_lost')}, "
                    f"{r('inbound_video_frame_width')}, {r('inbound_video_frame_height')}, {r('inbound_video_frames_per_second')},"
                    f"{r('inbound_video_frames_decoded')}, {r('inbound_video_frames_decoded_per_second')}, "
                    f"{r('inbound_video_frames_received')}, {r('inbound_video_frames_dropped')})")

        cursor.execute(add_stat)

    db.commit()
    cursor.close()
    db.close()





if __name__ == '__main__':
    interview_title = 'someinterview1'
    interview_status = 'ongoing'
    user_name = 'respondent2'
    peer_connection = '18084-9'
    peer_connection_type = 'outbound'
    stat_name = 'outbound_audio_packets_sent_per_second'
    date_time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    stat_value = '30'
    inbound_audio_packets_received_per_second = 50
    inbound_audio_bytes_received_per_second = 2345
    inbound_audio_packets_lost = 9
    inbound_audio_jitter = 45
    inbound_audio_jitter_buffer_delay = 3
    inbound_audio_total_samples_received = 8754
    inbound_audio_level = 82
    inbound_audio_energy = 732
    inbound_audio_round_trip_time = 32

    add_stats_row_to_database(interview_title=interview_title, interview_status=interview_status, user_name=user_name,
                              date_time_stamp=date_time_stamp, peer_connection=peer_connection, peer_connection_type=peer_connection_type,
                              inbound_audio_packets_received_per_second=inbound_audio_packets_received_per_second,
                              inbound_audio_bytes_received_per_second=inbound_audio_bytes_received_per_second,
                              inbound_audio_packets_lost=inbound_audio_packets_lost,
                              inbound_audio_jitter=inbound_audio_jitter,
                              inbound_audio_jitter_buffer_delay=inbound_audio_jitter_buffer_delay,
                              inbound_audio_total_samples_received=inbound_audio_total_samples_received,
                              inbound_audio_level=inbound_audio_level,
                              inbound_audio_energy=inbound_audio_energy,
                              inbound_audio_round_trip_time=inbound_audio_round_trip_time)