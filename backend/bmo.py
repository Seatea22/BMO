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

                string = await self.audio_manager.start_recording()
                print(string)

            elif user_input == "q":
                break

            else:
                print("Invalid input dummy")

            time.sleep(2)
            print("loop ran")

        return 0

    def audio_recording_start(self) -> int:
        """
        :return: 
        """

        if self.state != States.IDLE:
            return 0

        self.state = create_state(States.RECORDING)
        print(f"{self.process_name} has started {self.state}")

        self.audio_manager.start_recording()
