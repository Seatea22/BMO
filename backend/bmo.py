import asyncio
import time
from uuid import uuid4

from backend.audio import AudioManager
from state.state import States, create_state


class BMO:
    def __init__(self):
        self.process_name = "BMO_" + str(uuid4().time)
        self.state = create_state(States.IDLE)
        self.audio_manager = AudioManager()

    async def input_registration_loop(self):
        while True:
            # Replace this with button registry
            user_input = input("Enter input: ")

            if user_input == "r":

                string = await self.audio_recording_start()
                print(string)

            elif user_input == "q":
                break

            else:
                print("Invalid input dummy")

            time.sleep(2)
            print("loop ran")

        return 0

    async def audio_recording_start(self) -> str:
        """
        :return: 
        """

        if self.state.return_enum() != States.IDLE:
            return "Not in idle state"

        self.state = create_state(States.RECORDING)
        print(f"{self.process_name} has started {self.state}")

        return_value = await self.audio_manager.start_recording()
        if return_value == "Recording finished":
            self.state = create_state(States.DISPLAYING)
            print(return_value)
            await asyncio.sleep(2)
            self.state = create_state(States.IDLE)

        else:
            self.state = create_state(States.ERROR)
            print(return_value)
            await asyncio.sleep(2)
            self.state = create_state(States.IDLE)
