#!/usr/bin/env python3

import urllib

import discord
from discord.ext import commands

import logging

BASE_URL_MEME = "https://n303p4.github.io/{0}.html?{1}"

class Meme:

    def mogrify(self, template:str, **kwargs):
        """Meme generation.
        
        * template - The name of the template to use.
        * **args - The arguments to use in the format.
        """
        params = urllib.parse.urlencode(kwargs)
        url = BASE_URL_MEME.format(template, params)
        return url

    @commands.command(aliases=["um", "umeme", "standard"])
    @commands.cooldown(6, 12, commands.BucketType.user)
    async def usermeme(self, ctx, top_line:str, bottom_line:str, *, member:discord.Member=None):
        """Create a meme of a user. Use quotes around your arguments.
        
        Example usage:
        
        * kit usermeme \"This is\" "A meme\"
        * kit usermeme \"This is\" "A meme\" @Kitsuchan
        """
        if not member:
            member = ctx.author
        url_avatar = member.avatar_url.replace(".webp", ".png")
        url = self.mogrify("standard", title=" / ".join((top_line, bottom_line)),
                           image=url_avatar, top=top_line, bottom=bottom_line)
        embed = discord.Embed(title=f"{member.display_name} as a standard meme!")
        embed.description = f"[Click here to view]({url})"
        await ctx.send(embed=embed)

    @commands.command(aliases=["poster"])
    @commands.cooldown(6, 12, commands.BucketType.user)
    async def wanted(self, ctx, *, member:discord.Member=None):
        """Create a wanted poster of a user.
        
        Example usage:
        
        * kit wanted
        * kit wanted @Kitsuchan
        """
        if not member:
            member = ctx.author
        url_avatar = member.avatar_url.replace(".webp", ".png")
        url = self.mogrify("wanted", title=f"WANTED: {member.display_name}",
                           image=url_avatar)
        embed = discord.Embed(title=f"WANTED: {member.display_name}!")
        embed.description = f"[Click here to view]({url})"
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Meme())