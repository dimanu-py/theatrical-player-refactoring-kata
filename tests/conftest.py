from approvaltests.reporters import GenericDiffReporter, GenericDiffReporterConfig


class IntelliJDiffReporter(GenericDiffReporter):
    def __init__(self):
        config = GenericDiffReporterConfig(
            name="IntelliJ IDEA",
            path="/Applications/IntelliJ IDEA.app/Contents/MacOS/idea",
            extra_args=["diff"]
        )
        super().__init__(config)
