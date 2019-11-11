has_ticket = True
knife_length = 23

if has_ticket :
    print('Ticket check passed,prepare a safety check!')
    if knife_length > 20 :
        print('Arrest Him! He got a %dcm long knife' % knife_length)
    else:
        print('Safety check passed, have a good trip!')
else:
    print('fk off and buy a ticket')