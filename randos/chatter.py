def chatter():
    print 'welcome matey'
    print 'do ye choose the plank, or swab the decks?'

    answer = raw_input('what does ye choosen: plank or ye decks? ').lower()

    if answer == 'plank':
        print 'ye\'s a brave sumvabitch'
    elif answer == 'decks':
        print "ye's a dirty wench I see"
    else:
        print "answer me or I'll shoot you out me cannon!"
        chatter()

chatter()
