TOKEN = '7100898536:AAHSIACamXvQq0pW7QVHOvDR5GqS8MGxCLk'
# import asyncio
# import aiohttp
# import json

# async def curr_request():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://www.themealdb.com/api/json/v1/1/list.php?c=list') as resp:
#             categories_data = await resp.json()
#             categories = [cat['strCategory'] for cat in categories_data['meals']]
#             for category in categories:
#                 print(category, type(category))

# asyncio.run(curr_request())