import asyncio

import openai


async def openai_get_gpt_response(
    text_request: str,
    model: str,
    max_tries_number: int = 10,
    sleep_time: int = 3,
) -> str:
    response = ""
    is_success = False
    try_number = 0
    while not is_success and try_number < max_tries_number:
        response = (
            await openai.ChatCompletion.acreate(
                model=model,
                messages=[{"role": "user", "content": text_request}],
            )
        )["choices"][0]["message"]["content"]

        is_success = not any(i in response.lower() for i in ["sorry", "apologize"])
        try_number += 1
        if not is_success:
            print("Oops, something went wrong. Trying again (%s)...", try_number)
            await asyncio.sleep(sleep_time)

    return response


async def openai_get_generated_image_url(prompt: str, size: str = "1024x1024") -> str:
    response = await openai.Image.acreate(
        prompt=prompt,
        n=1,
        size=size,
    )
    return response["data"][0]["url"]
