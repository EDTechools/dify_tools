import base64
import hashlib
import hmac
import logging
import time
import urllib.parse
from typing import Any, Union

import httpx
from e2b_code_interpreter import CodeInterpreter

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool


class DingTalkGroupBotTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        """
            invoke tools
            Dingtalk custom group robot API docs:
            https://open.dingtalk.com/document/orgapp/custom-robot-access
        """
        code = tool_parameters.get('code')
        if not code:
            return self.create_text_message('Invalid parameter code')

        api_key = tool_parameters.get('api_key')
        if not api_key:
            return self.create_text_message('Invalid parameter api_key. ')

        api_url = 'https://oapi.dingtalk.com/robot/send'

        with CodeInterpreter(api_key=api_key) as sandbox:
            execution = sandbox.notebook.exec_cell(code)
            return self.create_text_message(execution.text)

