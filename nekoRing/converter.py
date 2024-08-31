import json

sites = [
[
    "https://webring.nekoweb.org/",
    "Webring Site <em>main site</em>",
    "The website you are on right now!",
  ],
  [
    "https://max.nekoweb.org/",
    "Max <em>manager</em>",
    "idiot web developer who tries to do things whenever i can, im also the manager of this webring!",
  ],
  ["https://glitchy404.nekoweb.org/", "Glitchy"],
  [
    "https://wiki.nekoweb.org/",
    "Dean/DeanTheExtreme",
    "The Nekoweb Wiki, documenting the free static web hosting Nekoweb.",
  ],
  [
    "https://nullcell.neocities.org/",
    "null",
    "piece of art a result of cool wisdom I possess. Everything is mostly variable bcoz I am interested in various fields.",
  ],
  [
    "https://lilith.nekoweb.org/",
    "Lilith",
    "WIP personal website. I plan to talk about things I am interested in",
  ],
  [
    "https://gif.nekoweb.org/",
    "hk",
    "A dump of my thoughts, images, music and most importantly gifs!",
  ],
  [
    "https://silas.nekoweb.org/",
    "silas",
    "the personal website of a queer transfag furby guy. ft. webdev bookmarks and more!",
  ],
  [
    "https://wynn.nekoweb.org/",
    "ThatOneUnoriginal",
    "A personal website for my online personality.",
  ],
  [
    "https://pyralspyte.nekoweb.org/",
    "gabriel",
    "the funny silly place.. just my personal site ^_^",
  ],
  [
    "https://raze3344.nekoweb.org/",
    "raze3344",
    "yo how do we use these &lt;div&gt; tags :P cuz i wanna do some cool stuff like u ^^",
  ],
  [
    "https://nekkostarr.nekoweb.org/",
    "Starr",
    "My site is a place to put random stuff I make ranging from an I.S.S. tracker to a flipnote still gallery, and more!",
  ],
  [
    "https://angelnetcast.nekoweb.org/",
    "angel",
    "a custom website for personal and fan content!",
  ],
  ["https://fish.nekoweb.org/", "?", "?"],
  [
    "https://lilly.nekoweb.org/",
    "lilly",
    "personal site!!! theres konata and cool tunes and stamps and kitties!!!",
  ],
  [
    "https://laura.nekoweb.org/",
    "Laura Sofia",
    "A silly trans hobby game dev and 15 year long web dev trying to be more unhinged when it comes to websites on my new page.",
  ],
  [
    "https://s1nez.nekoweb.org/",
    "ren",
    "im gay for v2 *fire writing gif* also i draw and animate and make music sometimes i guessss also im a sparklefur",
  ],
  [
    "https://angle.nekoweb.org/",
    "angle",
    "a personal site inspired by a geometry dash level.. Made to share whatever i feel like",
  ],
  [
    "https://picea.nekoweb.org/",
    "kat",
    "a storage closet for all my old projects. and other stuff too idk",
  ],
  ["https://lain.nekoweb.org/", "?", "?"],
  [
    "https://apfel.nekoweb.org/me/",
    "Ocram Ratte",
    "A site that features an about me section, status, links and updates on my projects.",
  ],
  ["https://toa.nekoweb.org/", "toa", "hi I'm toa and i like art and my OCs!"],
  [
    "https://autumn.nekoweb.org/",
    "autumn",
    'its my message in a bottle within the sea of messages in bottles. quick rundown of who i may be n wha i like to do n whatever may be "new" with me',
  ],
  [
    "https://corvidae.digital/",
    "corvidae",
    "this is my personal site where i cram as many things as i want into a compact little box :3 i share my creations, blogs, resource lists, graphics hoards, and more in here!",
  ],
  ["https://green.nekoweb.org/", "Green", "website for my stuff mainly :)"],
  ["https://remblanc.com/", "remblanc 1.x", "the personal website of all time"],
  [
    "https://pe3rl.nekoweb.org/",
    "Pe3RL",
    "dude i dont even know what html is i am frankensteining this shit together and praying it functions even slightly",
  ],
  ["https://valley.nekoweb.org/", "?", "?"],
  [
    "https://lapislabel.net/",
    "Lapis",
    "A sailor’s trinket box showcasing art, video games and other things of the nature!",
  ],
  [
    "https://evie.nekoweb.org/",
    "Evie",
    "a place for me to be both extremely queer <i>and</i> a terrible writer",
  ],
  ["https://woocat.nekoweb.org/", "woocat", "woocat webpage"],
  ["https://nekocat.nekoweb.org/", "nekocat", "home of the nekoweb cat"],
  [
    "https://pure.nekoweb.org/",
    "safiya",
    "a virtual curation of beauty and love found in the world hand coded by an 18 year old fashion student",
  ],
  [
    "https://wobbachu.nekoweb.org/",
    "Wobbachu",
    "The Wii-inspired personal website of artist Wobbachu, for your enjoyment, with a dash of pokémon for good measure!",
  ],
  ["https://jemmaontheweb.nekoweb.org/", "jemma", "Jemma, on the web"],
  [
    "https://astro.nekoweb.org/",
    "Astro/AstroLumin",
    "Random personal website full of cool stuff :)",
  ],
  [
    "https://xan.nekoweb.org/",
    "Xan on nekoweb",
    "Has some music and text and links, including one to their own domain",
  ],
  [
    "https://oposh.nekoweb.org/",
    "Oposh",
    "A personal site that belongs to opossum called Oposh",
  ],
  [
    "https:// /",
    "April",
    "Personal site where i share my hobbies and other stuff",
  ],
  [
    "https://mypillowfort.net/",
    "Shai",
    "A personal blog that offers over 3,000 cutesy graphics to you, the visitor, for free! Enjoy (´ ω `♡)",
  ],
  [
    "https://crystal.nekoweb.org/",
    "Crystal",
    "Personal site for OCs and Hatsune Miku.",
  ],
  [
    "https://vrz.nekoweb.org/",
    "Astral",
    "Astral's NekoWeb home page, always being worked on.",
  ],
  [
    "https://squidcrusher.nekoweb.org/",
    "Sam",
    "Personal website for a queer blogger who is autistic and really wants to show you its pet sites",
  ],
  [
    "https://octosquigglez.nekoweb.org/",
    "OctoSquigglez",
    "personal site filled to the brim with my hyperfixations (probably)",
  ],
  [
    "https://nekoaerospace.nekoweb.org/",
    "Neko CA",
    "Personal website for a random neko who's really big into spaceflight and is trying to learn HTML",
  ],
  [
    "visualdot.is-a.dev",
    "raidopaizer",
    "dumb basic webpage made by a freshman who uses gentoo linux",
  ],
  [
    "https://lime360.nekoweb.org",
    "lime360",
    "Lime's personal website. Formerly hosted on Neocities.",
  ],
  [
    "https://districts.nekoweb.org",
    "Districts",
    "Districts is a Nekoweb site directory (a pre-Y2k internet concept designed to help you more easily find webfronts by sorting them into relevant categories)!",
  ],
  [
    "https://tepiloxtl.net/",
    "Tepiloxtl @ Nekoweb",
    "Personal site I tippy-tap on about tech or games or who knows what actually :)",
  ],
  [
    "https://lel.nekoweb.org/",
    "Lel's Cult",
    "The most lelmaxxed site on nekoweb",
  ],
  [
    "https://felixfever.nekoweb.org/",
    "Felix FEVER",
    "Shrine to Fix-It Felix, Jr.",
  ],
  ["https://suavesuede.nekoweb.org", "?", "?"],
  [
    "https://dariusaur.nekoweb.org/",
    "LegenDarius",
    'A personal site with multiple layers of irony and satire, so you can never truly know who "Darius" is.',
  ],
  [
    "https://yummyicecream.nekoweb.org/",
    "yummyicecream",
    "a website that is kinda like the 1990s.",
  ],
  [
    "https://frizzbees.dev/",
    "bee",
    "personal site which hosts my blog among some other things :3",
  ],
  [
    "https://juno.nekoweb.org/",
    "juno",
    "deranged yuri + rhythm game fan headquarters",
  ],
  ["https://mved.nekoweb.org/", "guavasalt", "gup's sillay little aquarium"],
  [
    "https://quwyou.com/",
    "quwyou",
    "personal site lol. doesn't have much on it as of now",
  ],
  [
    "https://aurath.nekoweb.org/",
    "aurath",
    "my personal site that has a non zero amount of tsumugi aoba because i love him",
  ],
  [
    "https://akatsuki.nekoweb.org/",
    "Akatsuki's website",
    "My personal website, along with all my projects and nekosearch",
  ],
  ["https://penguinjaa.com/"],
  ["https://realismomagico.nekoweb.org/"],
  ["https://cherie.nekoweb.org/"],
  ["https://fujoshi.nekoweb.org"],
  ["https://evehibi.nekoweb.org"],
  ["https://bufucat.nekoweb.org/"],
  [
    "https://theabsoluterealm.com/",
    "shinto",
    "my personal website that houses my happy place and mind space, varying around gaming, references, easter eggs, art, programming, and more!",
  ],
  ["https://iluvwerewolves.nekoweb.org"],
  [
    "https://housepen.nekoweb.org",
    "Benggu",
    "A personal site hosting my art, blog, and animal crossing obsession",
  ],
  [
    "https://rice.nekoweb.org/",
    "ricebowl",
    "think of this site as a bowl of rice with various meats on top and a hint of stir fried bok choy.",
  ],
  ["https://july.lol"],
  [
    "https://thinliquid.dev",
    "thinliquid",
    "overstimulating catppuccin-infused portfolio/personal website!",
  ],
  ["https://arti1688.nekoweb.org"],
  ["https://reocities.nekoweb.org/"],
  ["https://giikis2.nekoweb.org/"],
  ["https://astralily.nekoweb.org/"],
  [
    "https://banami.nekoweb.org/",
    "Banami",
    "Banami (aka Achlys)'s Nekoweb! A super kewl personal site about me, riddled with sheer tons of nonsense!"
  ],
  ["https://effe-tei.nekoweb.org/"],
  ["https://saurmandal.nekoweb.org/"],
  ["https://caekpuppi.nekoweb.org/"],
  ]

def process_sites(data):
    processed_data = {"sites": []}
    for site in data:
        url = site[0]
        name = site[1] if len(site) > 1 else "n/a"
        desc = site[2] if len(site) > 2 else "n/a"
        site_entry = {
            "name": name,
            "url": url,
            "desc": desc,
        }
        processed_data["sites"].append(site_entry)
    return processed_data

output = process_sites(sites)

with open('sitesNekoRing.json', 'w') as f:
    json.dump(output, f, indent=2)

print("finished !!")
