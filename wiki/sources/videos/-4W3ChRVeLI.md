---
title: "Beyond Kubernetes Security - Ellen Körbes, Tilt & Tabitha Sable, Datadog"
video: -4W3ChRVeLI
kind: concept
orgs: []
topics: ["kubernetes security", "threat modeling", "threat morphology", "attack surface"]
---

# Beyond Kubernetes Security - Ellen Körbes, Tilt & Tabitha Sable, Datadog

concept · 42:12 · [Watch on YouTube](https://www.youtube.com/watch?v=-4W3ChRVeLI)

Playlists: [KubeCon + CloudNativeCon North America 2021](../PLj6h78yzYM2Nd1U4RMhv7v88fdiFqeYAP.md)

> Explores security threats that go beyond Kubernetes itself, starting from threat morphology.

Topics: `kubernetes security`, `threat modeling`, `threat morphology`, `attack surface`

## Transcript

[▶ 0:00](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=0s) hey everybody um you know like it like it says here i'm i'm tablets able and this is beyond kubernetes security uh thank you so much especially the people that are coming in virtual like i know it's really hard to do yet another virtual con especially when you're like know that there's there's some people that are here in la it is wonderful here in la but i'm so so glad especially for those of y'all who couldn't make it for showing up here so let's let's get started um does this look good can everybody sweep all right cool so um to move beyond kubernetes security the first thing that we're going to need

[▶ 0:42](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=42s) to do is understand threat morphology so there's these threats that you already know about like you know about internal threats you know like uh like a malicious contractor or uh or a disgruntled employee and external threats like the nsa the gru you know a board kid in ukraine oh oh gosh what what what's going on i'm i'm sorry uh you don't know me yet but by the end of this talk you're presenting right now we're gonna be lifelong friends i need you to know that the curse it wasn't really a curse but i'm sorry

[▶ 1:25](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=85s) this is going to make more sense later i'm going to be broadcasting you some things i'm sorry but they might be slightly harder i'm so sorry i i don't know what's going on um this thank you thank you all for for putting up with this with this interruption [Music] hello [Music] um

[▶ 2:42](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=162s) [Music] oh

[▶ 3:47](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=227s) uh hey um yeah this is tabitha i'm i'm so confused ukraine oh oh no i don't think i'm going to be able to do the presentation i think we're going to have to deal with this from the future telling me to use this thing to stand here yeah i'm i'm i'm really confused too but

[▶ 4:30](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=270s) like i'm supposed to tell you about what happened when i was in pripyat in in 2013 and like i'm not actually allowed to talk about that so this must be really really serious last try during person but never thanks for the chance not you me come back oh my god yeah whatever um um yeah i'm gonna try to wipe myself really you need to come back this is this is so bad like

[▶ 5:14](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=314s) we need to talk hi i suppose this is tabitha i was told to talk to you apparently whatever you were doing in 2013 um i was told it's happening i was told this would make sense to you and that he would help so whoever you are yeah what's going on yeah yeah i'll help um hey uh so yeah this is this is really awkward but when i got out of school back in the 90s like was until just a few years ago when i

[▶ 5:58](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=358s) got started doing cloud native security i was working on a project that i can't really talk about it started out as a surveillance system called the heptagon network but we we expanded it over time and it turned into like a multi-dimensional ai powered defense system called sky cloud with with the things that have been happening to you i think i'm afraid you're being targeted by sky cloud okay wait i'm i'm getting all worked up because like some pile of back scrubs doing linear regression called sky clouds trying to actually there's okay

[▶ 6:42](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=402s) that's enough for you oh no no no you you don't know what you're getting into you need to you need to slow down okay look uh i i don't know who you are but um i've been doing this for a while i know what i'm doing so have i and i'm telling no ellen please i'm trying to help but you're you're gonna need really serious planning or you're actually just going to get yourself in more trouble please call me back wherever you are hey tommy uh sorry i'm doing garbage

[▶ 7:25](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=445s) collection here on the whole time thing and the last worst house favorite can you forward her sorry i mean me the me you you were just talking to not me here that you know that me uh foreigner the third email you got from retuken in 1998. and yeah just for the email uh i'll route it to the right time and you know yeah the whole thing but yeah just trust me that this is a lot easier for him okay [Music]

[▶ 8:26](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=506s) oh my god it's been so long since i had to read japanese um okay so like you were reading about buffer overflows and you found one in the login page that we wrote and you wrote an exploit for the back end code but the real login page is protected by input validation so like it's probably okay goodness uh that that could save us i hope that after 25 years it still works um i'm i'm gonna forward you the email now um tell me tell me if you get it if i just got your email i didn't realize we're gonna help you with this i said i'm gonna help you yeah yeah i'm like i think if you run that code from that attachment inside

[▶ 9:10](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=550s) the heptagon network i think it'll be able to crash the the like sky cloud control system and and i think it'll save your life uh [Music] [Music]

[▶ 10:02](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=602s) foreign [Music] um [Music] is [Music]

[▶ 10:58](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=658s) m foreign [Music] [Music] [Music]

[▶ 11:54](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=714s) we have this thing that can only do like single commands at a time i don't think we can run uh retsuko's search exploit with this so can you at least help me with this i mean yeah of course i can help you with this like not every vulnerability has an exploit that's super convenient to use but like put malware on the thing and give yourself whatever you know whatever quality of life things that you need i don't think you even need anything fancy just like normal pen testing tools are probably going to be good enough um [Music]

[▶ 13:03](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=783s) foreign [Music] [Music] we we got

[▶ 13:48](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=828s) what you said uh what now well you're in like congratulations you win the game do the thing that you want to do look around the system figure out the situation escalate to root and run the exploit code this thing's running on kubernetes i'm sure you can figure out a way to be able to to be able to run something oh oh it's a kubernetes system i know this um um

[▶ 14:44](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=884s) [Music] [Music] [Music] operation not permitted

[▶ 16:11](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=971s) okay fellow 69 blocked his class [Music] foreign [Music] of course it failed i'm

[▶ 17:02](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1022s) look i'm trying not to like i know you're under a lot of pressure right now but like you could have checked out what was going on before you went and just tried to run some some exploits like their clusters looks like it's really well configured and managed i'm surprised they even needed a kernel update but you know i guess just patch is actually a lot harder than it sounds even for the heptagon and sky cloud okay and what that is wrong you should have checked out the situation more thoroughly like sure their colonel was vulnerable but you got totally iced out anyway like that kernel

[▶ 17:46](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1066s) bug needs capnet admin to be able to trigger it which you don't have fortunately a lot of mainstream linux distros allow unprivileged users to spawn username spaces and you can get capnet admin within your username space great so now all of that kernel attack surface is available to you but there's an alpha feature in kubernetes 1.22 called set comp default if you enable the feature gate and the kubelet and then set the kubelet config that turns it on then it takes advantage of some really good set comp filtering that jesse frizzell and some other fabulous hackers did years ago like it blocks a few really weird sis calls that normal applications have no business calling

[▶ 18:30](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1110s) anyway like onshare which is what you need to be able to spawn a username space and so most applications can just run under it but also it can sometimes shut down attacks like yours oh um okay so do i need to find like a different vulnerability that doesn't need that that's this call mean that's a thing you could do but like it may not be that easy did you notice you didn't have any good linux capabilities in your bounding set when you looked at my container they've got their workloads pretty locked down like if they're using really up-to-date things like they may have turned on pod

[▶ 19:13](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1153s) security admission that's another alpha feature from 1.22 and it looks like they were ready to try it as soon as it was available so like if they're doing that to enforce policy about what kinds of dangerous pop features can be used in what name spaces like you may struggle to find a pod that has enough permissions to do anything dangerous so like you can keep plugging away at it and try and find another bug but can you do it before they catch you so what can i do i mean it really doesn't seem like you're going to be able to pound the front door down like this they're really well prepared

[▶ 19:57](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1197s) for direct attacks so i think you're going to need to attack them indirectly just try the usual things you fish a developer commit some malicious code into their test suite wait for the cicd system to run the test code easy just commit some malicious code hello hello yourself oh hi what's up so remember when we did this like that time ooh do i get to get you out of trouble again like old times well yeah like old times so here's the deal yeah and then she told

[▶ 20:42](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1242s) me to fish a developer basically i can't believe you're dragging me into this again okay do you know who works at the company um i do not check linkedin okay okay ceo hr that guy gandalf looks interesting who's he oh my god check this out oh gee hacker one of the last real hackers and then he shares a link to a retrospective on the glory days of something something sounds just like you used to so i bet his whole networking setup is just

[▶ 21:26](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1286s) like the good old days too if you know what i mean tabby uh so we we got this guy i i found him on irc uh this is uh this is where his connection is coming from i'm i mapped it and this is what it gave me do you know anything about this wait wait what is that open ssh 2.3 this is hilarious that oh my gosh so there was this protocol vulnerability in in ssh1 where the the checksum that was being used was not strong enough so like you could cause collisions and decrypt the

[▶ 22:09](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1329s) encrypted traffic like cool great like that was dangerous and a lot of people caused a lot of trouble so the developers put some code into the damon that would detect when that attack was being performed against the server and like shut it down but you know how these things go the attack detection code also had vulnerabilities in it oh my gosh everybody was like hacking servers all day long with that thing back in the day found it i think i found something what do you make of this attacks against open ssh security incidents mailing aircrafts okay um open ssh 2.2 upon

[▶ 22:52](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1372s) something this is the crc exploit i think this is what happy said this should do the trick now if only we could get our hands on this puppy wait hold up team teso 2001 that's didn't you get a whole stash of exploits from back then from that friend of yours what's her face oh yeah you're right lex murphy dave's sister you're right give me a minute [Music] sweet

[▶ 23:44](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1424s) okay uh cat oh lord it's in the write-up dummy right you're right this is working oh yeah look at that yes just a couple times okay let me let me get into the code um doesn't work here um just be a good girl and do as i say [Music] script slash dev slash null control z

[▶ 24:27](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1467s) now stty size stdy raw [Music] you're welcome okay so did this oh it did cool um tubby we're in what do we do next what do you do next you have access to their source code on the on the developers home network like i don't know why they're letting them do that but like good for us right stick the kill switch into the test suite let

[▶ 25:10](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1510s) the build server run it and like live free another day what just do it so this will make their tests run the two case binary which they do and unsigned commit oh uh whatever oh goodness okay still stop stop that's it um now how do we check this how do we how do we know if this works i don't know check his email okay good idea um and of course his favorite email client is okay so i guess now we just sit and wait huh um in the meantime tabby um can you tell

[▶ 25:54](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1554s) me how the zag spike actually works a little bit so like the main fail safe for the sky cloud system was that all seven delegates of the heptagon network needed to be present to start it up once it's started it can lose nodes and keep running but if it's shut completely down they have to restart it together and there's only one node left okay but who even are these people this this is so strange oh you you don't even know who they all are ellen there there was the pentagon there was like a couple of other countries antarctica the moon

[▶ 26:38](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1598s) and like nobody's really sure who the last two delegates were like i'm i'm not actually convinced that they were human okay looks like we got mail cat listen to this um you're commit something something has failed to build due to error and welcome it's signature potential tempering detected counter measures active of course can't this is this is not good no it's not uh what's your escape plan there's because real talk you might be in actual trouble maybe i can escape plan i i'll try something else i'll figure

[▶ 27:21](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1641s) something out but but can't you ow can if oh if i get you in trouble again shut up no i'll tell you when i'm out let's keep going are you sure let's keep going tabby um things went wrong what else can we do yeah i mean of course things went wrong nobody enforces mandatory commit signing just because it's fun they're doing it in order to secure their software so like with their system set up to have signatures on commits validated in the build system anything like what you're trying to do is going to be a dead end unless you can

[▶ 28:05](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1685s) get access to the developer's private keys so like i think you're kind of stuck on this go after the other end go after delivery like if you can push a malicious container into their repository and then overwrite existing tags for containers that they're using then like the next time a pod dies or they scale up or something like that like they won't even know the difference they'll just slurp down your new container think it's the old one and run it and then you win okay so i was looking around and i i think we got a good candidate let's try hijacking the images for this database maintenance operator

[▶ 28:49](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1729s) [Music] what the hell build system is this i don't think it's a build system it looks more like a development environment is code kind of a thing so it looks like here's where it makes the call to create the images and here's the actual image it generates okay let's start this thing up oh wow this is cool so easy even your attacker can figure it out huh yeah well at least i can um okay let me add um that code in here okay yeah yeah let's do that build that thing okay

[▶ 29:32](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1772s) looks like we're done here before i ship this tabby what did i do rob this time i mean for once i think you got it right like you tested your changes locally so you know the container will work when they run it push it in there like congratulations you're learning cat um so we gotta do the devopsy stuff now um how do i do the you know the image switcheroo thing so what you gotta do is overwrite the image tag right first get the id of the image that tool just built for you with docker images

[▶ 30:16](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1816s) then tag it with the same name but with the remote registry okay do it with docker tag the image id then the remote registry slash the image name right yep now check it with docker images good and off we go docker push remote registry slash tag oh my god and there you go you did this okay how do i check um how do i save the thing check their observability dash look for any logs from db maintenance and see the brand okay so beta dog logs uh jp maintenance yeah this is what we wanted um well yeah

[▶ 31:00](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1860s) keep control of energy logs strategically sync sync failed with admission webhook container failed signature validation potential tempering oh counter measures activated oh oh can't i think this is when you tell me around yeah i'm sorry it didn't work yeah um cat all logs delete our pictures delete like hell i don't know mixtapes um everything it's safe for you if if we never mind

[▶ 31:47](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1907s) l yeah i hope you get out of this okay me too tubby what can we do next time i'm out of ideas darker

[▶ 32:42](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=1962s) oh oh my gosh i'm i'm i'm so sorry they're their defense is really cutting edge there's so much work going on right now around ensuring kubernetes clusters only run trusted images like i was just at kubecon and like i swear half the talks are about software supply chain security like people really are thinking about this like for example there's an admission controller called connoisseur that can check container image signatures before it runs before it lets them run um projects like sig store tough and in total we're making it easier than ever to like ship things that are signed so that they are validated

[▶ 33:25](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=2005s) some organizations are building on this work with like even more sophisticated private tools that maybe we'll seek it open source someday of course the heptagon has integrated custom container image verification into their kubernetes clusters like you're just caught i don't think there's anything else we can do unless you could like send yourself back in time before they were so well defended like i'm sorry i'm i don't know what i can do to help you hi debbie uh i'm sorry it's it's been a few weeks since you last saw it anyway [Music]

[▶ 34:42](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=2082s) [Music] i'm [Music] uh

[▶ 35:24](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=2124s) i was just joking about that time travel thing but like cool let's do it okay oh [Music] [Music] transformation

[▶ 36:18](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=2178s) [Music] uh if you can modify their legacy code that's still running even though it was written back in like 1997 i maybe you would be able to get those changes in well before any of this focused on security started happening [Music] maybe today their defense wouldn't be able to save them um i don't know if that's a thing you can do though the math took a little bit to figure out we did it and by we i mean lucas did all the work so um [Music]

[▶ 37:30](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=2250s) so it's gonna be tricky but there's a chance good good luck ellen i'm gonna go make some calls uh i need to go call myself in the beginning of this whole story even so see you in 1997 and hopefully i can uh so i can make it back uh on this event foreign oh my god

[▶ 38:21](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=2301s) they're really in 1997. here i am it's 1997 and uh yeah i'm ready i i i can't believe it um wait wait i'm worried they might somehow find this bug in the like 25 years between then and now what if you made the kill switch mechanism only appear for a couple of minutes like during kubecon oh i can only appear for two minutes yeah that's that's a good idea okay yeah yeah let's do that oh we shouldn't do that though because

[▶ 39:05](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=2345s) like the schedule can be weird and like what if my talk runs over and we don't have the timing right um i don't know you probably shouldn't tell me i am literally streaming to your exact time right now i know what time it is okay if you're if you're sure i'm gonna hang up for good now i'm gonna do the hack you're gonna have those two minutes to get in there after that i'm gonna have to label for a while you're gonna know if i made it out okay or not by i don't know check my twitter see you back in the future maybe not

[▶ 39:49](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=2389s) goodbye guess i'm gonna start by connecting to their network and downloading their repo so here they are what can we do here let's see source code libraries login yeah okay this is what i want let me use these libraries so i'm going to fill the buffer that ritsuka had talked about here filling hashtag with a large pile of garbage and okay if this crashes it's gonna crash sky cloud let's see yes and i'm back to the future

[▶ 41:01](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=2461s) well [Music] i i think they're alive thank you all all right like real talk i don't actually know what time it is but i know we were right up to the lunch break so like can we do questions do we have questions yeah i guess we won't have official

[▶ 41:50](https://www.youtube.com/watch?v=-4W3ChRVeLI&t=2510s) questions but like i'll be happy to put my mask on and and talk to folks thank you all again so much for coming thank you you
