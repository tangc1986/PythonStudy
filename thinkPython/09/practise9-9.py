for i in range(11, 100):
    me = i
    mather = i%10*10 + i/10
    if me >= mather: continue
    count = 0
    age_width = mather - me
    for age in range(0, me):
        me_age = age
        mather_age = age + age_width
        if me_age%10 == mather_age/10 and me_age/10 == mather_age%10:
            count = count + 1
    if count == 5:
        all_count = 0
        for age in range(0, 150):
            me_age = age
            mather_age = age + age_width
            if me_age%10 == mather_age/10 and me_age/10 == mather_age%10:
                all_count = all_count + 1
        if all_count == 8:
            print me
            

        