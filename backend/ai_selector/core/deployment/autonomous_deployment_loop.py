class AutonomousDeploymentLoop:

    def __init__(
        self,
        validator,
        deployer,
        switcher
    ):
        self.validator = validator
        self.deployer = deployer
        self.switcher = switcher


    def deploy(
        self,
        policy
    ):

        if not self.validator.validate(policy):
            return False


        deployed = self.deployer.deploy(
            policy
        )


        self.switcher.switch(
            deployed
        )


        return True