"""Inbound Audio"""

def get_inbound_audio_packets_received_per_second(stats_data):
    title = 'inbound_audio_packets_received_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPAudioStream') and key.endswith('[packetsReceived/s]'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_audio_bytes_received_per_second(stats_data):
    title = 'inbound_audio_bytes_received_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPAudioStream') and key.endswith('[bytesReceived_in_bits/s]'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_audio_packets_lost(stats_data):
    title = 'inbound_audio_packets_lost'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPAudioStream') and key.endswith('packetsLost'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_audio_jitter(stats_data):
    title = 'inbound_audio_jitter'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPAudioStream') and key.endswith('jitter'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_audio_jitter_buffer_delay(stats_data):
    title = 'inbound_audio_jitter_buffer_delay'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPAudioStream') and key.endswith('jitterBufferDelay'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_audio_total_samples_received(stats_data):
    title = 'inbound_audio_total_samples_received'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPAudioStream') and key.endswith('totalSamplesReceived'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_audio_level(stats_data):
    title = 'inbound_audio_level'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPAudioStream') and key.endswith('audioLevel'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_audio_energy(stats_data):
    title = 'inbound_audio_energy'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPAudioStream') and key.endswith('totalAudioEnergy'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_audio_round_trip_time(stats_data):
    title = 'inbound_audio_round_trip_time'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPAudioStream') and key.endswith('roundTripTime'):
           return_data.append({key: value})
    return title, return_data


"""Inbound Video"""

def get_inbound_video_packets_received_per_second(stats_data):
    title = 'inbound_video_packets_received_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('[packetsReceived/s]'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_video_bytes_received_per_second(stats_data):
    title = 'inbound_video_bytes_received_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('[bytesReceived_in_bits/s]'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_video_packets_lost(stats_data):
    title = 'inbound_video_packets_lost'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('packetsLost'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_video_frame_width(stats_data):
    title = 'inbound_video_frame_width'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('frameWidth'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_video_frame_height(stats_data):
    title = 'inbound_video_frame_height'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('frameHeight'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_video_frames_per_second(stats_data):
    title = 'inbound_video_frames_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('framesPerSecond'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_video_frames_received(stats_data):
    title = 'inbound_video_frames_received'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('framesReceived'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_video_frames_decoded(stats_data):
    title = 'inbound_video_frames_decoded'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('framesDecoded'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_video_frames_decoded_per_second(stats_data):
    title = 'inbound_video_frames_decoded_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('[framesDecoded/s]'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_video_frames_dropped(stats_data):
    title = 'inbound_video_frames_dropped'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('framesDropped'):
           return_data.append({key: value})
    return title, return_data[0]


def get_inbound_video_round_trip_time(stats_data):
    title = 'inbound_video_round_trip_time'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCInboundRTPVideoStream') and key.endswith('roundTripTime'):
           return_data.append({key: value})
    return title, return_data[0]


"""Outbound Audio"""

def get_outbound_audio_packets_sent_per_second(stats_data):
    title = 'outbound_audio_packets_sent_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPAudioStream') and key.endswith('[packetsSent/s]'):
           return_data.append({key: value})
    return title, return_data


def get_outbound_audio_bytes_sent_per_second(stats_data):
    title = 'outbound_audio_bytes_sent_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPAudioStream') and key.endswith('[bytesSent_in_bits/s]'):
           return_data.append({key: value})
    return title, return_data


"""Outbound Video"""

def get_outbound_video_packets_sent_per_second(stats_data):
    title = 'outbound_video_packets_sent_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPVideoStream') and key.endswith('[packetsSent/s]'):
           return_data.append({key: value})
    return title, return_data


def get_outbound_video_bytes_sent_per_second(stats_data):
    title = 'outbound_video_bytes_sent_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPVideoStream') and key.endswith('[bytesSent_in_bits/s]'):
           return_data.append({key: value})
    return title, return_data


def get_outbound_video_frames_encoded(stats_data):
    title = 'outbound_video_frames_encoded'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPVideoStream') and key.endswith('framesEncoded'):
           return_data.append({key: value})
    return title, return_data


def get_outbound_video_frames_encoded_per_second(stats_data):
    title = 'outbound_video_frames_encoded_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPVideoStream') and key.endswith('[framesEncoded/s]'):
           return_data.append({key: value})
    return title, return_data


def get_outbound_video_frames_sent(stats_data):
    title = 'outbound_video_frames_sent'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPVideoStream') and key.endswith('framesSent'):
           return_data.append({key: value})
    return title, return_data


def get_outbound_video_quality_limitation_reason(stats_data):
    title = 'outbound_video_quality_limitation_reason'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPVideoStream') and key.endswith('QualityLimitationReason'):
           return_data.append({key: value})
    return title, return_data


def get_outbound_video_quality_limitation_resolution_change(stats_data):
    title = 'outbound_video_quality_limitation_resolution_change'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPVideoStream') and key.endswith('QualityLimitationResolutionChange'):
           return_data.append({key: value})
    return title, return_data


def get_outbound_video_frame_width(stats_data):
    title = 'outbound_video_frame_width'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPVideoStream') and key.endswith('frameWidth'):
           return_data.append({key: value})
    return title, return_data


def get_outbound_video_frame_height(stats_data):
    title = 'outbound_video_frame_height'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPVideoStream') and key.endswith('frameHeight'):
           return_data.append({key: value})
    return title, return_data


def get_outbound_video_frames_per_second(stats_data):
    title = 'outbound_video_frames_per_second'
    return_data = []
    for key, value in stats_data.items():
        if key.startswith('RTCOutboundRTPVideoStream') and key.endswith('framesPerSecond'):
           return_data.append({key: value})
    return title, return_data








