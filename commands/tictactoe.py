from discord.ext import commands
import discord

class tictactoe(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases = ["ttt"])
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def tictactoe(self, ctx, member: discord.Member):
		await ctx.trigger_typing()
		if member.bot:
			return await ctx.send("That is a bot! Please play against a person!")
		if member.id == ctx.author.id:
			return await ctx.send("You can't challenge yourself silly!")
		message = await ctx.send(f"{member.mention}, {ctx.author.mention} wants to play tic-tac-toe with you! Do you accept?")
		await message.add_reaction("✅")
		await message.add_reaction("❌")
		global validGame
		validGame = None
		def check1(payload):
			global validGame
			if (str(payload.emoji) == "❌" or str(payload.emoji) == "✅") and payload.message_id == message.id and payload.member.id == member.id:
				validGame = str(payload.emoji)
				return True
		try:
			await self.bot.wait_for("raw_reaction_add", check = check1, timeout = 60)
			if not validGame == "✅":
				await message.edit(content = "The user has declined your request!")
				return
			else:
				await message.delete()
		except TimeoutError:
			await message.edit(content = "The user has not reacted in time!")
			return
		players = [{"type":"❌", "id": ctx.author.id, "member": ctx.author.name},{"type":"⭕", "id": str(member.id), "member": member.name}]
		global player
		player = -1
		board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
		reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
		def displayBoard():
			newBoard = []
			num = -1
			for x in board:
				num += 1
				condition = " " if not num in [3, 6] else "\n"
				newBoard.append(f"{condition}{x if not str(x).isnumeric() else reactions[num]}")
			return "".join(newBoard)
		def makeMove(ctx, pos):
			global player
			if str(board[pos]).isnumeric():
				board[pos] = players[player]["type"]
				player = (player + 1) % len(players)
			else:
				return False
		embed = discord.Embed(title = "Tic-Tac-Toe!", description = displayBoard(), color = discord.Colour.random())
		message = await ctx.send(content = f"It's {players[player]['member']}'s turn!", embed = embed)
		for Reaction in reactions:
			await message.add_reaction(Reaction)
		def check(payload):
			global reaction
			reaction = str(payload.emoji)
			if str(payload.emoji) in reactions and str(payload.message_id) == str(message.id) and str(payload.member.id) == str(players[player]["id"]):
				return True
		def is_winner():
			global player
			possibleWins = [
				[1, 2, 3],
				[4, 5, 6],
				[7, 8, 9],
				[1, 4, 7],
				[2, 5, 8],
				[3, 6, 9],
				[1, 5, 9],
				[3, 5, 7]
			]
			state = board
			X = []
			O = []
			num = 0
			for x in state:
				num += 1
				if x == "❌":
					X.append(num)
				if x == "⭕":
					O.append(num)
				for win in possibleWins:
					winner = None
					winListX = []
					winListO = []
					for Win in win:
						if Win in X:
							winListX.append(Win)
						if Win in O:
							winListO.append(Win)
						if str(win) == str(winListX):
							winner = "X"
							break
						if str(win) == str(winListO):
							winner = "O"
							break
					if winner != None:
						break
			global Player
			Player = players[(player + 1) % len(players)]["member"]
			return winner
		def is_tie():
			tie = []
			for x in board:
				if str(x).isnumeric():
					return False
				else:
					tie.append("1")
				if len(tie) >= 9:
					return True
		while is_winner() == None and is_tie() == False:
			try:
				await self.bot.wait_for("raw_reaction_add", check = check, timeout = 60)
				global reaction
				pos = reactions.index(f"{reaction}")
				if makeMove(ctx, pos) == False:
					await ctx.send("That spot is taken!")
				embed = discord.Embed(title = "Tic-Tac-Toe!", description = displayBoard(), color = discord.Colour.random())
				await message.edit(content = f"It's {players[player]['member']}'s turn!", embed = embed)
			except TimeoutError:
				return await ctx.send("The game has ended as no one reacted in a minute")
		global Player
		if is_tie() == True:
			await message.edit(content = f"It's a tie!", embed = embed)
			return
		await message.edit(content = f"{Player} won!", embed = embed)

def setup(bot):
	bot.add_cog(tictactoe(bot))