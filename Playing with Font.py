import discord
from discord.ext import commands
from constants import TOKEN

# intents = discord.Intents.default()
# intents.members = True
client = commands.Bot(command_prefix='!')

@client.command()
async def italic(ctx):
    response = 'This text has some words *emphasized* in _different_ ways'
    await ctx.send(response)

@client.command()
async def bold(ctx):
    response = 'This text has **important** words in it. Use \*\* to make your text bold'
    await ctx.send(response)

@client.command()
async def underline(ctx):
    response = '__This text is underlined for emphasis__'
    await ctx.send(response)

@client.command()
async def strike(ctx):
    response = 'Their house was ~~large~~ enormous'
    await ctx.send(response)

@client.command()
async def secret(ctx):
    secret = 'Darth Vader'
    response = "❗Spoiler ahead❗\n||{}|| is Luke Skywalker's father".format(secret)
    await ctx.send(response)

@client.command()
async def block_quote(ctx, *, arg):
    quote_text = 'You said:\n> {}'.format(arg)
    await ctx.send(quote_text)

@client.command()
async def multi_quote(ctx, *args):
    one_word_per_line = '\n'.join(args)
    quote_text = 'You said:\n>>> {}'.format(one_word_per_line)
    await ctx.send(quote_text)

@client.command()
async def inline_code(ctx):
    response = 'Use the `discord.py` module to make a Discord bot in Python!'
    await ctx.send(response)

@client.command()
async def code_examples(ctx):
    examples = """```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[][] a = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                a[i][j] = in.nextInt();
                System.out.print(a[i][j] + " ");
            }
        }
    }
}
    ```
    """
    
    await ctx.send(examples)


@client.command()
async def embed(ctx):
    embed=discord.Embed(
    title="Text Formatting",
        url="https://realdrewdata.medium.com/",
        description="Here are some ways to format text",
        color=discord.Color.blue())
    embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://cdn-images-1.medium.com/fit/c/32/32/1*QVYjh50XJuOLQBeH_RZoGw.jpeg")
    #embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    embed.add_field(name="*Italics*", value="Surround your text in asterisks (\*)", inline=False)
    embed.add_field(name="**Bold**", value="Surround your text in double asterisks (\*\*)", inline=False)
    embed.add_field(name="__Underline__", value="Surround your text in double underscores (\_\_)", inline=False)
    embed.add_field(name="~~Strikethrough~~", value="Surround your text in double tildes (\~\~)", inline=False)
    embed.add_field(name="`Code Chunks`", value="Surround your text in backticks (\`)", inline=False)
    embed.add_field(name="Blockquotes", value="> Start your text with a greater than symbol (\>)", inline=False)
    embed.add_field(name="Secrets", value="||Surround your text with double pipes (\|\|)||", inline=False)
    embed.set_footer(text="Learn more here: realdrewdata.medium.com")
    await ctx.send(embed=embed)

client.run(TOKEN)