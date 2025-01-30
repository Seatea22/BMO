from uuid import uuid4

from state.state import States, create_state
class BMO:
    def __init__(self):
        self.process_name = "BMO_" + str(uuid4().time)
        self.state = create_state(States.IDLE)

        print(f"Started {self.process_name} with state: {self.state}")

