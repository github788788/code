exec(open('util.py').read())
def rumble_gen(inp):
	rumble_urls = []

	#<iframe src="https://rumble.com/embed/v4spnbx/?pub=3i4h9q"></iframe>
	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__description__")
	new.append("__rumble_embed_url__")
	rumble_urls.append(new)

	new = []
	new.append("arizona")
	new.append("lankford")
	new.append("130 thousand illegal votes were cast in Nevada")
	new.append("https://rumble.com/embed/v4spnbx/?pub=3i4h9q")
	rumble_urls.append(new)

	new = []
	new.append("georgia")
	new.append("Joseph Rossi")
	new.append("Georgia Recount Violated Georgia Election Law")
	new.append("https://rumble.com/embed/v4r928i/?pub=3i4h9q")
	rumble_urls.append(new)

	new = []
	new.append("georgia")
	new.append("??")
	new.append("Over 300,000 ballot images lost Georgia 2020 recount (Fulton county)")
	new.append("https://rumble.com/embed/v4rayvc/?pub=3i4h9q")
	rumble_urls.append(new)

	new = []
	new.append("michigan")
	new.append("??")
	new.append("Van Drops of Ballots in Middle of Night")
	new.append("https://rumble.com/embed/v4qyb7l/?pub=3i4h9q")
	rumble_urls.append(new)

	new = []
	new.append("michigan")
	new.append("Jim Runestad")
	new.append("(R) Michigan State Senator")
	new.append("Explanation of Voter Michigan Fraud")
	new.append("https://rumble.com/embed/v4qvtai/?pub=3i4h9q")
	rumble_urls.append(new)

	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__description__")
	new.append("__rumble_embed_url__")
	rumble_urls.append(new)

	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__description__")
	new.append("__rumble_embed_url__")
	rumble_urls.append(new)


	base_html = """

        <div id="__new_row__" class="gjs-grid-row">
                <div id="ies45" class="gjs-grid-column">
                        <div id="it87s" class="gjs-grid-row">
                                <div id="i9l46" class="gjs-grid-column">
                                        <div id="i0joh">arizona</div>
                                </div>
                        </div>
                </div>
                <div id="ihbee" class="gjs-grid-column">
                        <div id="iitt2" class="gjs-grid-row">
                                <div class="gjs-grid-column">
                                        <div id="iocj3"><iframe frameborder="0"
                                                        src="https://rumble.com/embed/v4qvth5/?pub=3i4h9q"
                                                        id="arizona1-2"></iframe></div>
                                </div>
                                <div id="i2owo" class="gjs-grid-column">
                                        <div id="i6lauy"><iframe frameborder="0"
                                                        src="https://rumble.com/embed/v4qvth5/?pub=3i4h9q"
                                                        id="arizona2"></iframe></div>
                                </div>
                                <div class="gjs-grid-column">
                                        <div id="imt6xh"><iframe frameborder="0"
                                                        src="https://rumble.com/embed/v4qvth5/?pub=3i4h9q"
                                                        id="arizona3"></iframe></div>
                                </div>
                        </div>
                </div>
        </div>
        """

	
inp = []
rumble_gen(inp)