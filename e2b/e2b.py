from core.tools.provider.builtin.e2b.tools.e2b_code_bot import E2BCodeBotTool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController


class E2BCodeProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: dict) -> None:
        E2BCodeBotTool()
        pass
