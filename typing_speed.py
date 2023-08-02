import curses
import time
import random

A = [
    "A cat and a dog chased a ball in the park.",
    "An apple a day keeps the doctor away.",
    "I have a black hat and a blue bag.",
    "The alarm clock rang as I woke up.",
    "He ate a large pizza and a juicy apple.",
    "The rain started as the sun hid behind a cloud.",
    "She danced gracefully to the music.",
    "A small ant crawled on the wall.",
    "The artist drew a beautiful landscape.",
    "The baby laughed and clapped its hands."
]
B = [
    "The big brown bear roamed in the forest.",
    "A blue bird flew over the river.",
    "She bought a basket full of fruits.",
    "He built a sturdy bridge over the stream.",
    "I baked banana bread for breakfast.",
    "The bright butterfly fluttered in the garden.",
    "The baseball game was exciting.",
    "She wore a beautiful blue dress.",
    "The bookshelf in the corner was filled with books.",
    "He was busy with his business trip."
]
C = [
    "The clever cat caught a fish.",
    "She wore a colorful coat in the cold.",
    "A cute little puppy played in the park.",
    "I cooked chicken curry for dinner.",
    "The curious child asked many questions.",
    "The car raced down the highway.",
    "He closed the window to keep out the cold.",
    "She carried a heavy bag full of groceries.",
    "The chef cooked delicious cookies.",
    "The clock struck twelve as the party began."
]
D = [
    "The dog barked loudly at the mailman.",
    "He danced with delight at the party.",
    "A delicious dinner was served on the table.",
    "She dared to climb the highest mountain.",
    "The dark night was calm and peaceful.",
    "I downloaded a new game on my computer.",
    "The doctor examined the patient carefully.",
    "The diamond ring sparkled in the sunlight.",
    "They decided to visit the nearby zoo.",
    "The door creaked as it opened slowly."
]
E = [
    "The elephant is the largest land animal.",
    "She earned a gold medal for her performance.",
    "We enjoyed the evening by the lake.",
    "The eagle soared high in the sky.",
    "I entered the room and saw a beautiful painting.",
    "The exercise routine helped improve my health.",
    "He eagerly awaited the results of the competition.",
    "A strong earthquake shook the city.",
    "She explained the concept in a simple way.",
    "The event ended with a grand celebration."
]
F= [
    "I found a lost kitten near my house.",
    "The firefighters rushed to the burning building.",
    "She played the flute at the school concert.",
    "He wore a fashionable outfit to the party.",
    "The fox hid behind the tall grass.",
    "A friendly smile can brighten someone's day.",
    "They fixed the broken fence in the backyard.",
    "The fragrance of flowers filled the air.",
    "I forgot to bring my umbrella in the rain.",
    "She finished her work before the deadline."
]
G= [
    "The green grass grew in the garden.",
    "He gave a great speech at the conference.",
    "The grapes were sweet and juicy.",
    "I glanced at the clock and realized it was late.",
    "She gently placed the gift on the table.",
    "The guitar player strummed the chords.",
    "The glowing moon appeared in the night sky.",
    "They gathered around the bonfire and sang songs.",
    "The giggling children played in the park.",
    "The golden sunset painted the sky."
]
H= [
    "He had a habit of humming while working.",
    "I held her hand as we walked together.",
    "The horse galloped across the open field.",
    "She hugged her friend tightly.",
    "The hawk soared high above the mountains.",
    "I heard the sound of laughter from the other room.",
    "The helicopter flew over the city.",
    "The hiking trail led to a hidden waterfall.",
    "The hotel had a beautiful view of the ocean.",
    "They happily danced at the wedding."
]
I= [
    "I am excited to visit the new amusement park.",
    "She is studying information technology.",
    "The ice cream shop offered a variety of flavors.",
    "I invited my friends to my birthday party.",
    "The idea of going on a vacation sounded fun.",
    "The insect crawled on the flower petal.",
    "I included some extra notes in the presentation.",
    "She invested her time in learning new skills.",
    "The illustrator drew colorful illustrations for the book.",
    "I ignored the noise and focused on my work."
]
J= [
    "Jack jumped over the candlestick.",
    "The jellyfish gracefully swam in the ocean.",
    "He joined a jazz band as a drummer.",
    "The jacket kept her warm in the cold weather.",
    "I just received a message from my friend.",
    "The journalist interviewed the famous actor.",
    "She juggled colorful balls at the circus.",
    "The jewelry store had a stunning collection.",
    "The jury carefully considered the evidence.",
    "I jogged around the park for exercise."
]
K= [
    "The kind king ruled the kingdom with compassion.",
    "She kicked the ball with all her strength.",
    "The kids played happily in the playground.",
    "The kitchen was filled with the aroma of freshly baked cookies.",
    "He knew the secret key to solving the puzzle.",
    "I keep my keys in the front pocket of my bag.",
    "The knight protected the castle from intruders.",
    "The kitten purred as it cuddled with its owner.",
    "The kangaroo hopped across the vast desert.",
    "The kite soared high in the sky on a windy day."
]
L= [
    "The little girl picked up the colorful flowers.",
    "He looked at the lovely landscape painting.",
    "The lion roared loudly in the jungle.",
    "The laptop is on the table next to the lamp.",
    "She likes to read books with adventurous plots.",
    "The light from the lantern illuminated the path.",
    "I left my umbrella at the library yesterday.",
    "The lizard crawled up the wall and disappeared.",
    "He learned to play the guitar with dedication.",
    "The leaves on the trees turned yellow in autumn."
]
M= [
    "The magical magician entertained the audience.",
    "The moon shines brightly in the night sky.",
    "He made a mistake but quickly corrected it.",
    "The melody of the music touched my heart.",
    "I met my friends at the movie theater.",
    "The monkey swung from branch to branch.",
    "The mountain peak was covered in snow.",
    "She wore a mask to protect herself.",
    "The mechanic fixed the broken car.",
    "The map showed the way to the treasure."
]
N= [
    "The naughty child played pranks on his siblings.",
    "She needs to finish her homework before dinner.",
    "The nurse took care of the sick patients.",
    "The newspaper reported the latest news.",
    "He never gives up, no matter the challenges.",
    "I noticed the beautiful flowers in the garden.",
    "The night sky was filled with stars.",
    "I navigated through the maze to find the exit.",
    "The necklace was a gift from her grandmother.",
    "The novel kept me engaged till the last page."
]
O= [
    "The orange is a juicy and delicious fruit.",
    "I observed the behavior of the wild animals.",
    "She opened the door to let in fresh air.",
    "The ocean waves crashed against the shore.",
    "He offered to help his friend with the project.",
    "The owl hooted in the quiet night.",
    "I ordered a pizza for dinner.",
    "The orchestra played a beautiful symphony.",
    "The old man sat on the park bench.",
    "The office was buzzing with activity."
]
P= [
    "The playful puppy chased its tail.",
    "The parrot repeated the words I said.",
    "She painted a pretty picture of a flower.",
    "The plane flew high above the clouds.",
    "I prepared a delicious pasta dish for lunch.",
    "The powerful punch knocked out the opponent.",
    "The police officer protected the city.",
    "The patient patiently waited for the doctor.",
    "I packed my bag for the weekend trip.",
    "He pressed the button to turn on the computer."
]
Q= [
    "The quiet library is a great place to study.",
    "She quickly solved the difficult math question.",
    "The queen wore a beautiful gown to the ball.",
    "The quacking ducks swam in the pond.",
    "I queued up to buy tickets for the show.",
    "The quality of the product is excellent.",
    "The question puzzled me for a long time.",
    "I quoted a famous line from the movie.",
    "The quilt kept her warm on a cold night.",
    "He quenched his thirst with a glass of water."
]
R= [
    "The rabbit hopped away into the woods.",
    "She read a thrilling novel by the author.",
    "I rode my bike to the park.",
    "The raindrops fell gently from the sky.",
    "He ran quickly to catch the bus.",
    "The river flowed gracefully through the valley.",
    "She reached for the red apple on the tree.",
    "The robot performed tasks efficiently.",
    "The road led to a beautiful beach.",
    "I received a letter from my friend."
]
S= [
    "The sun set behind the mountains.",
    "She sang a sweet melody.",
    "The snake slithered silently through the grass.",
    "I sat on the swing at the playground.",
    "The ship sailed across the vast ocean.",
    "He smiled and said hello to everyone.",
    "She skillfully played the piano.",
    "The stars shone brightly in the night sky.",
    "I swam in the cool and refreshing water.",
    "The scientist conducted experiments in the lab."
]
T= [
    "The tiger is a majestic and powerful animal.",
    "She typed a long document on her laptop.",
    "I tasted the delicious cake at the bakery.",
    "The tree stood tall in the middle of the field.",
    "He tried his best to solve the puzzle.",
    "The train arrived at the station on time.",
    "She talked to her friend on the phone.",
    "The teacher explained the lesson clearly.",
    "I took a walk in the park in the morning.",
    "The traffic on the road was heavy during rush hour."
]
U= [
    "I used a blue pen to write the letter.",
    "The umbrella protected me from the rain.",
    "She used her skills to create a masterpiece.",
    "The unicorn is a mythical and magical creature.",
    "I understand the importance of hard work.",
    "The university offers various courses.",
    "He used a map to navigate through the forest.",
    "The utensils were neatly arranged in the kitchen.",
    "She unlocked the door with a key.",
    "The universe is vast and full of mysteries."
]
V= [
    "The violinist played a beautiful melody.",
    "The vibrant colors brightened up the room.",
    "I visited the famous art museum.",
    "The volcano erupted with a loud noise.",
    "She volunteered to help at the charity event.",
    "The victory was celebrated with enthusiasm.",
    "He voiced his opinion during the meeting.",
    "The van drove along the winding road.",
    "I value the time spent with family.",
    "The vegetables were fresh and healthy."
]
W= [
    "The white rabbit hopped quickly.",
    "She wore a warm winter coat.",
    "I watched a funny video online.",
    "The waves crashed against the shore.",
    "He went for a walk in the woods.",
    "The waiter served delicious food.",
    "She waved goodbye to her friends.",
    "I walked to the nearby park.",
    "The weather was warm and sunny.",
    "The whale is a massive sea creature."
]
X= [
    "The xylophone made a pleasant sound.",
    "She had to fix a broken axle.",
    "I received an expensive gift.",
    "The box was full of chocolates.",
    "The fox has a bushy tail.",
    "The taxi driver took the shortest route.",
    "I mixed the colors to create a new shade.",
    "She used an x-ray to examine the patient.",
    "The extra effort paid off in the end.",
    "The exercise routine helped improve my health."
]
Y= [
    "The yellow sun rose in the sky.",
    "She wore a pretty yellow dress.",
    "I yelled for help when I was stuck.",
    "The yacht sailed gracefully on the water.",
    "He played the guitar with skill.",
    "The yogi practiced yoga every morning.",
    "She received a heartfelt letter.",
    "The young child was full of energy.",
    "The yogurt was creamy and delicious.",
    "I enjoyed the view of the mountains."
]
Z= [
    "The zebra has black and white stripes.",
    "She zoomed in on the tiny details.",
    "I zipped up my jacket to stay warm.",
    "The zoo is a fun place to visit.",
    "He played the xylophone with zeal.",
    "I gazed at the zodiac constellations.",
    "The zigzag path led to the mountain top.",
    "She was amazed by the dazzling fireworks.",
    "The zealous athlete trained hard for the competition.",
    "I snoozed for a while in the afternoon."
]

uc=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def start_screen(stdscr):
	stdscr.clear()
	stdscr.addstr(0,0,"Welcome to the Speed Typing Test!",curses.A_BOLD)
	stdscr.addstr(1,0,"Press Select a letter to begin!",curses.A_BOLD)
    
	r= int((curses.COLS/2)-(52))
	curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_WHITE)
	for x in uc:
	    stdscr.addstr(2,r,f" {x} ",curses.color_pair(3))
	    r+=3
	    stdscr.addstr(2,r," ")
	    r+=1
	stdscr.refresh()
	stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
	stdscr.addstr(target)
	stdscr.addstr(1, 0, f"WPM: {wpm}")

	for i, char in enumerate(current):
		correct_char = target[i]
		color = curses.color_pair(1)
		if char != correct_char:
			color = curses.color_pair(2)

		stdscr.addstr(0, i, char, color)

def load_text():
    lines = ["The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How quickly daft jumping zebras vex.",
    "Jinxed wizards pluck ivy from the big quilt.",
    "The five boxing wizards jump quickly.",
    "Bright vixens jump; dozy fowl quack.",
    "We promptly judged antique ivory buckles for the next prize.",
    "Crazy Fredrick bought many very exquisite opal jewels.",
    "The job requires extra pluck and zeal from every young wage earner."]

    return random.choice(lines).strip()

def wpm_test(stdscr):
	target_text = load_text()
	current_text = []
	wpm = 0
	start_time = time.time()
	stdscr.nodelay(True)

	while True:
		time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

		stdscr.clear()
		display_text(stdscr, target_text, current_text, wpm)
		stdscr.refresh()

		if "".join(current_text) == target_text:
			stdscr.nodelay(False)
			break

		try:
			key = stdscr.getkey()
		except:
			continue

		if ord(key) == 27:
			break

		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
			current_text.append(key)

def main(stdscr):
	curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
	curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
	start_screen(stdscr)
	while True:
		try:
			wpm_test(stdscr)
			stdscr.addstr(2,0,"You completed the text!\nPress Esc to exit or \nPress any key to continue...")
		except:
			stdscr.addstr(2,0,"An Error occurred!\nPress Esc to exit or \nPress any key to continue...")
		key = stdscr.getkey()
		if ord(key)==27:
		    curses.endwin()
		    break

def test(stdscr): 
    stdscr.clear()
    stdscr.addstr(0,0,"Welcome to the Speed Typing Test!",curses.A_BOLD)
    stdscr.addstr(1,0,"Press Select a letter to begin!",curses.A_BOLD)
    s=r= int((curses.COLS/2)-(52))
    curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_WHITE)
    for x in uc:
	    stdscr.addstr(2,r,f" {x} ",curses.color_pair(3))
	    r+=3
	    stdscr.addstr(2,r," ")
	    r+=1
    stdscr.addstr(3,s-1,"")
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(test)