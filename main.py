"""Example shows how to send requests and get responses."""

import asyncio

from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, StartStreamingRequest,StartRecordingRequest,StartStopRecordingRequest,ToggleMuteRequest,SetCurrentSceneRequest,GetVolumeRequest,EnableStudioModeRequest
from obswsrc.types import Stream, StreamSettings


async def main():

    async with OBSWS('localhost', 4444, "1234") as obsws:

        # We can send an empty StartStreaming request (in that case the plugin
        # will use OBS configuration), but let's provide some settings as well
        stream_settings = StreamSettings(
            server="rtmp://example.org/my_application",
            key="secret_stream_key",
            use_auth=False
        )
        stream = Stream(
            settings=stream_settings,
            type="rtmp_custom",
        )

        # Now let's actually perform a request
        response = await obsws.require(EnableStudioModeRequest())
        response = await obsws.require(GetVolumeRequest(source="a"))
        print(response)
        response = await obsws.require(SetCurrentSceneRequest(scene_name="On Arrive"))

        response = await obsws.require(ToggleMuteRequest(source="a"))
#         response = await obsws.require(StartStopRecordingRequest())

#         response = await obsws.require(StartRecordingRequest())
#         response = await obsws.require(StartStreamingRequest(stream=stream))
    print(response)
#         # Check if everything is OK
#         if response.status == ResponseStatus.OK:
#             print("Streaming has started")
#         else:
#             print("Couldn't start the stream! Reason:", response.error)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
