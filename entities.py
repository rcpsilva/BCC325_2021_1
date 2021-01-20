class Agent():
    """
        Implements the interface for an Agent
    """
    def __init__(self,env):
        """
        Constructor for the agent class

        Args:
            env: a reference to an environment
        """

        self.env = env

    def act(self):
        """
        Defines the agent action

        Raises:
           NotImplementedError: If the method is not implemented or not overridden.
        """

        raise NotImplementedError('act')

class Environment:
    """
        Implements the interface for an Environment
    """
    def initial_percepts(self):
        """
        Returns the enviroment initial percepts

        Raises:
            NotImplementedError: If the method is not implemented or not overridden.
        """

        raise NotImplementedError('initial percepts')

    def signal(self,action):
        """
        Returns the enviroment percepts after action is executed.

        Raises:
            NotImplementedError: If the method is not implemented or not overridden.
        """
        raise NotImplementedError('signal')


        

