def event_preprocessing(df):
    df['id'] = df['id'].astype(str)
    # categorical columns with a name parameter
    obj_to_int = lambda x: x['name'] if type(x)!=float else -1
    obj_cols = ['player','type','play_pattern', 'possession_team','team', 'position']
    for col in obj_cols:
        print(col, end='')
        df[col] = df[col].apply(obj_to_int)
        print('.... complete')
    
    #generic parameters that concern (nearly) all events regardless of type
    print('location', end='')
    df['location_available'] = df['location'].apply(lambda x: True if type(x)!= float else False) 
    df['location_x'] = df['location'].apply(lambda x: x[0] if type(x)!= float else 0)
    df['location_y'] = df['location'].apply(lambda x: x[1] if type(x)!= float else 0)
    print('.... complete')

    print('under_pressure', end='')
    df['under_pressure'] = df['under_pressure'].apply(lambda x: True if x==1 else False)
    print('.... complete')
    print('counterpress', end='')
    df['counterpress'] = df['counterpress'].apply(lambda x: True if x==1 else False)
    print('.... complete')
    print('off_camera', end='')
    df['off_camera'] = df['off_camera'].apply(lambda x: True if x==1 else False)
    print('.... complete')
    print('out', end='')
    df['out'] = df['out'].apply(lambda x: True if x==1 else False)
    print('.... complete')

    # columns regarding specific types of events

    print('carry', end='')
    df['carry_available'] = df['carry'].apply(lambda x: True if type(x)!= float else False)
    df['carry_endposition_x'] = df['carry'].apply(lambda x: x['end_location'][0] if type(x)!= float else -1)
    df['carry_endposition_y'] = df['carry'].apply(lambda x: x['end_location'][1] if type(x)!= float else -1)
    print('.... complete')

    print('ball_receipt', end='')
    df['ball_receipt_available'] = df['ball_receipt'].apply(lambda x: True if type(x)!=float else False)
    df['ball_receipt_outcome'] = df['ball_receipt'].apply(lambda x: x['outcome']['id'] if type(x)!=float else -1)
    print('.... complete')

    print('shot', end='')
    df['shot_available'] = df['shot'].apply(lambda x: True if type(x)!=float else False)
    df['shot_endlocation_x'] = df['shot'].apply(lambda x: x['end_location'][0] if type(x)!=float else -1)
    df['shot_endlocation_y'] = df['shot'].apply(lambda x: x['end_location'][1] if type(x)!=float else -1)
    df['shot_statbomb_xg'] = df['shot'].apply(lambda x: x['statsbomb_xg'] if type(x)!=float else -1)
    df['shot_outcome'] = df['shot'].apply(lambda x: x['outcome']['name'] if type(x)!=float else "No Shot")
    print('.... complete')
    # what do you mean by pass Id ?

    print('dribble', end='')
    df['dribble_available'] = df['dribble'].apply(lambda x: True if type(x)!=float else False)
    print('.... complete')

    print('pass', end='')
    df['pass_available'] = df['pass'].apply(lambda x: True if type(x)!=float else False)
    df['pass_end_location_x'] = df['pass'].apply(lambda x: x['end_location'][0] if type(x)!= float else -1)
    df['pass_end_location_y'] = df['pass'].apply(lambda x: x['end_location'][1] if type(x)!= float else -1)
    print('.... complete')

    # dropping columns
    df = df.drop(errors='ignore', columns= ['id','duration','timestamp','related_events', 'tactics', 'location', 'carry', 'ball_receipt', 'shot', 'dribble', 'miscontrol', 'bad_behaviour', 'substitution', 'pass'])
    return df

def drop_unprocessed(df):
    return df.drop(errors='ignore', columns= ['interception', 'ball_recovery','goalkeeper', 'clearance', 'block', 'foul_committed', 'foul_won', 'duel','possession'] )