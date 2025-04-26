langgraph.types.StateSnapshot(
    values={
        'messages': [
            HumanMessage(content='what is the capital of France? search by tavily', additional_kwargs={}, response_metadata={}, id='164f615b-4807-42ee-930a-98d93cf9d0bb'),
            AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_nwQVoYq2tIyzGOBsPIq4mwKA', 'function': {'arguments': '{"query":"capital of France"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 21, 'prompt_tokens': 90, 'total_tokens': 111, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_dbaca60df0', 'id': 'chatcmpl-BQaOaGcUkmm3pVHQvBzzjznDZZSbA', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-d7dd3634-552b-4c81-b46b-9e63ec5125f6-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'capital of France'}, 'id': 'call_nwQVoYq2tIyzGOBsPIq4mwKA', 'type': 'tool_call'}], usage_metadata={'input_tokens': 90, 'output_tokens': 21, 'total_tokens': 111, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})
        ]
    },
    next=('tools',),
    config={
        'configurable': {
            'thread_id': '1',
            'checkpoint_ns': '',
            'checkpoint_id': '1f022a70-b02c-695e-8001-c05e34256b15'
        }
    },
    metadata={
        'source': 'loop',
        'writes': {
            'bot': {
                'messages': [
                    AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_nwQVoYq2tIyzGOBsPIq4mwKA', 'function': {'arguments': '{"query":"capital of France"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 21, 'prompt_tokens': 90, 'total_tokens': 111, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_dbaca60df0', 'id': 'chatcmpl-BQaOaGcUkmm3pVHQvBzzjznDZZSbA', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-d7dd3634-552b-4c81-b46b-9e63ec5125f6-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'capital of France'}, 'id': 'call_nwQVoYq2tIyzGOBsPIq4mwKA', 'type': 'tool_call'}], usage_metadata={'input_tokens': 90, 'output_tokens': 21, 'total_tokens': 111, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})
                ]
            }
        },
        'step': 1,
        'parents': {},
        'thread_id': 1
    },
    created_at='2025-04-26T14:02:08.809994+00:00',
    parent_config={
        'configurable': {
            'thread_id': '1',
            'checkpoint_ns': '',
            'checkpoint_id': '1f022a70-a6d9-60be-8000-9c4b49a747bf'
        }
    },
    tasks=(
        langgraph.types.PregelTask(
            id='f26d9012-eb69-3902-fc38-dd0f86e92dc4',
            name='tools',
            path=('__pregel_pull', 'tools'),
            error=None,
            interrupts=(),
            state=None,
            result=None
        ),
    )
)
