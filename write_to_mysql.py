import mysql.connector
from datetime import datetime
from pprint import pprint


def r(key):
    if key in stat_tick.keys():
        return f"'{stat_tick[key]}'"
    else:
        return """'None'"""


def form_querry(peer_connection_id, peer_connection_data, parsed_stats, date_time_stamp):
    interview_status = 'Dummy_active'
    user_name = 'Dummy_name'
    peer_connection_type = peer_connection_data['connection_type']
    interview_id = peer_connection_data['interview_id']
    global stat_tick
    stat_tick = parsed_stats[date_time_stamp]

    unified_fields = ("INSERT IGNORE INTO test2 (interview, interviewStatus, userName, "
                      "dateTimeStamp, peerConnection, peerConnectionType, ")

    unified_data = f"VALUES ('{interview_id}', '{interview_status}', '{user_name}', " \
                   f"'{date_time_stamp}', '{peer_connection_id}', '{peer_connection_type}', "
    inbound_fields = (
        "InboundAudio_packetsReceivedS, InboundAudio_bytesReceived_in_bitsS, InboundAudio_packetsLost, "
        "InboundAudio_jitter, InboundAudio_jitterBufferDelay, InboundAudio_totalSamplesReceived, "
        "InboundAudio_audioLevel, InboundAudio_totalAudioEnergy,"
        # "InboundAudio_roundTripTime,"
        "InboundVideo_packetsReceivedS, InboundVideo_bytesReceived_in_bitsS, "
        "InboundVideo_packetsLost, "
        "InboundVideo_frameWidth, InboundVideo_frameHeight, InboundVideo_framesPerSecond, "
        "InboundVideo_framesDecoded, InboundVideo_framesDecodedS, "
        "InboundVideo_framesReceived, InboundVideo_framesDropped) "
        # "InboundVideo_roundTripTime,"
    )
    inbound_data = (
        f"{r('InboundAudio_[packetsReceived/s]')}, {r('InboundAudio_[bytesReceived_in_bits/s]')}, {r('InboundAudio_packetsLost')}, "
        f"{r('InboundAudio_jitter')}, {r('InboundAudio_jitterBufferDelay')}, {r('InboundAudio_totalSamplesReceived')}, "
        f"{r('InboundAudio_audioLevel')}, {r('InboundAudio_totalAudioEnergy')},"
        f"{r('InboundVideo_[packetsReceived/s]')}, {r('InboundVideo_[bytesReceived_in_bits/s]')}, "
        f"{r('InboundVideo_packetsLost')}, "
        f"{r('InboundVideo_frameWidth')}, {r('InboundVideo_frameHeight')}, {r('InboundVideo_framesPerSecond')},"
        f"{r('InboundVideo_framesDecoded')}, {r('InboundVideo_[framesDecoded/s]')}, "
        f"{r('InboundVideo_framesReceived')}, {r('InboundVideo_framesDropped')}"
        f")")

    outbound_fields = (
        "OutboundAudio_packetsSentS, OutboundAudio_bytesSent_in_bitsS,"
        "OutboundVideo_packetsSentS, OutboundVideo_bytesSent_in_bitsS, "
        "OutboundVideo_framesEncoded, OutboundVideo_framesEncodedS, "
        "OutboundVideo_framesSent, OutboundVideo_framesPerSecond, "
        # "OutboundVideo_QualityLimitationReason, "
        "OutboundVideo_QualityLimitationResolutionChange, "
        "OutboundVideo_frameWidth, OutboundVideo_frameHeight"
        ")")
    outbound_data = (
        f"{r('OutboundAudio_[packetsSent/s]')}, {r('OutboundAudio_[bytesSent_in_bits/s]')}, "
        f"{r('OutboundVideo_[packetsSent/s]')}, {r('OutboundVideo_[bytesSent_in_bits/s]')},"
        f"{r('OutboundVideo_framesEncoded')}, {r('OutboundVideo_[framesEncoded/s]')}, "
        f"{r('OutboundVideo_framesSent')}, {r('OutboundVideo_framesPerSecond')}, "
        # f"{r('qualityLimitationReason')}, "
        f"{r('OutboundVideo_qualityLimitationResolutionChanges')},"
        f"{r('OutboundVideo_frameWidth')}, {r('OutboundVideo_frameHeight')}"
        f")"
    )

    if peer_connection_type == 'inbound':
        querry = f"{unified_fields}{inbound_fields}{unified_data}{inbound_data}"
    elif peer_connection_type == 'outbound':
        querry = f"{unified_fields}{outbound_fields}{unified_data}{outbound_data}"
    return(querry)


def add_stats_row_to_database(parsed_peer_connections_data):
    db = mysql.connector.connect(host='10.1.10.106',
                                 port=3306,
                                 user='admin',
                                 password='admin',
                                 database='webrtcStatsTest')
    cursor = db.cursor()
    for peer_connection_id, peer_connection_data in parsed_peer_connections_data.items():
        parsed_stats = peer_connection_data['parsed_stats']

        for date_time_stamp in parsed_stats.keys():
            querry = form_querry(peer_connection_id, peer_connection_data, parsed_stats, date_time_stamp)
            cursor.execute(querry.encode('utf-8'))

    db.commit()
    cursor.close()
    db.close()

