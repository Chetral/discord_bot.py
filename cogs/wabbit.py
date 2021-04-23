import time
import discord
import psutil
import os
import asyncio
import json
import requests
import TenGiphPy



from datetime import datetime
from discord.ext import commands
from utils import default
from random import seed
from random import randint

class Wabbit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()
        self.process = psutil.Process(os.getpid())

    @commands.command()
    async def greet(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        """ greet sameone """
        if not user or user.id == ctx.author.id:
            msg_txt= f"**{ctx.author.display_name}** greets everyone!✌️"
        if user:
            msg_txt = f"**{user.display_name}**, **{ctx.author.display_name}** greets you!✌️"
            if user.id == self.bot.user.id:
                msg_txt= "*Greets himself*... sad..."
            if user.bot:
                msg_txt= f"**{ctx.author.display_name}** thanks to think also to us bot!✌️"
               
        embed = discord.Embed(title="Greets", description=msg_txt, colour=0x87CEEB, timestamp=datetime.utcnow())
        #embed.set_author(name="WabbitBot", icon_url=ctx.author.avatar_url)
        if reason != "":
            embed.add_field(name="Reason", value=reason, inline=False)
        #embed.set_footer(text="Wow! A footer!", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
        
        msg = await ctx.send(content="", embed=embed)
        
        embed2 = discord.Embed(title="Greets", description=f"**{user.display_name}** and **{ctx.author.display_name}** greets each other friendly! ✌️", colour=0x87CEEB, timestamp=datetime.utcnow())
        #embed2.set_author(name="WabbitBot", icon_url=ctx.author.avatar_url)
        embed3 = discord.Embed(title="Greets", description=f"Well, **{ctx.author.display_name}** seems that **{user.display_name}** doesn't want to greet you...", colour=0x87CEEB, timestamp=datetime.utcnow())
        #embed3.set_author(name="WabbitBot", icon_url=ctx.author.avatar_url)
        embed4 = discord.Embed(title="Greets", description=f"Ohps, **{ctx.author.display_name}** seems that **{user.display_name}** is upset with you! 🖕", colour=0x87CEEB, timestamp=datetime.utcnow())
        #embed4.set_author(name="WabbitBot", icon_url=ctx.author.avatar_url)

        
        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and (str(m.emoji) == "✌️" or str(m.emoji) == "🖕"):
                return True
            return False

        try:
            await msg.add_reaction("✌️")
            await msg.add_reaction("🖕")
            #await self.bot.wait_for('raw_reaction_add', timeout=30.0, check=reaction_check)
            reaction = await self.bot.wait_for('raw_reaction_add', timeout=20.0, check=reaction_check)
            if str(reaction.emoji) == "✌️":
                await msg.edit(embed=embed2)
            if str(reaction.emoji) == "🖕":
                await msg.edit(embed=embed4)
        except asyncio.TimeoutError:
            await msg.edit(embed=embed3)
        except discord.Forbidden:
            # Yeah so, bot doesn't have reaction permission, drop the "offer" word
            salu_offer = f"**{user.display_name}**, **{ctx.author.display_name}** greets you! ✌️"
            salu_offer = salu_offer + f"\n\n**Reason:** {reason}" if reason else salu_offer
            await msg.edit(content=salu_offer)

    @commands.command()
    async def hug(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        """ greet sameone """
        if not user:
            msg_txt= f"**{ctx.author.display_name}** hugs everyone!🤗"
        if user:
            msg_txt = f"**{user.display_name}**, **{ctx.author.display_name}** wants to hug you!🤗"
            if user.display_name == ctx.author.display_name:
                msg_txt= "*Hugs himself*... sad..."
            if user.bot:
                msg_txt= f"**{ctx.author.display_name}** thanks to think also to us bot!🤗"
               
        embed = discord.Embed(title="Hugs", description=msg_txt, colour=0x87CEEB, timestamp=datetime.utcnow())
        #embed.set_author(name="WabbitBot", icon_url=ctx.author.avatar_url)
        if reason != "":
            embed.add_field(name="Reason", value=reason, inline=False)
        #embed.set_footer(text="Wow! A footer!", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
        
        msg = await ctx.send(content="", embed=embed)
        
        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and (str(m.emoji) == "🤗" or str(m.emoji) == "🛑"):
                return True
            return False
            
        if user and user.display_name != ctx.author.display_name:
            try:
                await msg.add_reaction("🤗")
                await msg.add_reaction("🛑")
                reaction = await self.bot.wait_for('raw_reaction_add', timeout=20.0, check=reaction_check)
                if str(reaction.emoji) == "🤗":
                    lGif = await loadGif("anime,hug")
                    embed2 = discord.Embed(title="Hugs", type = "image", description=f"**{user.display_name}** and **{ctx.author.display_name}** hugs each other friendly! 🤗", colour=0x6AA84F, timestamp=datetime.utcnow())
                    await msg.delete()
                    await ctx.send(content="", embed=embed2)
                    await ctx.send(content=lGif)
                if str(reaction.emoji) == "🛑":
                    lGif = await loadGif("anime,hug,fail")
                    embed4 = discord.Embed(title="Hugs",type = "image", description=f"Ops, **{ctx.author.display_name}** seems that **{user.display_name}** doesn't want an hug from you! 🛑", colour=0xFF0000, timestamp=datetime.utcnow())
                    await msg.delete()
                    await ctx.send(content="", embed=embed4)
                    await ctx.send(content=lGif)
            except asyncio.TimeoutError:
                embed3 = discord.Embed(title="Hugs", description=f"Well, **{ctx.author.display_name}** seems that **{user.display_name}** doesn't want to hug you...", colour=0x87CEEB, timestamp=datetime.utcnow())
                await msg.edit(embed=embed3)
            except discord.Forbidden:
                # Yeah so, bot doesn't have reaction permission, drop the "offer" word
                salu_offer = f"**{user.display_name}**, **{ctx.author.display_name}** hugs you! 🤗"
                salu_offer = salu_offer + f"\n\n**Reason:** {reason}" if reason else salu_offer
                await msg.edit(content=salu_offer)

def setup(bot):
    bot.add_cog(Wabbit(bot))


def loadGif(tag):
    t = TenGiphPy.Tenor(token="SUAKQ62VFRJJ")
    getgifurl = t.arandom(str(tag))
    return getgifurl
