parsed_stat_list = {
    'RTCInboundRTPAudioStream': [
                                '[packetsReceived/s]',
                                '[bytesReceived_in_bits/s]',
                                'packetsLost',
                                'jitter',
                                'jitterBufferDelay',
                                'totalSamplesReceived',
                                'audioLevel',
                                'totalAudioEnergy',
                                'roundTripTime',
    ],
    'RTCInboundRTPVideoStream': [
                                '[packetsReceived/s]',
                                '[bytesReceived_in_bits/s]',
                                'packetsLost',
                                'frameWidth',
                                'frameHeight',
                                'framesPerSecond',
                                'framesReceived',
                                'framesDecoded',
                                '[framesDecoded/s]',
                                'framesDropped',
                                'roundTripTime',
    ],
    'RTCOutboundRTPAudioStream': [
                                '[packetsSent/s]',
                                '[bytesSent_in_bits/s]',
    ],
    'RTCOutboundRTPVideoStream': [
                                '[packetsSent/s]',
                                '[bytesSent_in_bits/s]',
                                'framesEncoded',
                                '[framesEncoded/s]',
                                'framesSent',
                                'QualityLimitationReason',
                                'QualityLimitationResolutionChange',
                                'frameWidth',
                                'frameHeight',
                                'framesPerSecond'
    ],
}