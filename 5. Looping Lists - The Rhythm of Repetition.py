# Task 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
counter = 0
track_message = "Track"
track_counter = 0
index = 0

for genre in genres:
    print(f"My favorite type of music to listen to is {genre}")
    counter += 1
    print(f" {track_message} {counter} : {genre}")
    


# Task 2
while True:
     for genre in genres:
      print(f"My type of music to listen to is {genre}")
      counter += 1
      #print(f" {track_message} {counter} : {genre}")
      
     #genre = genres[index]
     
     if genre == 'Classical':
          
          break
     
     #print(f"My favorite type of music to listen to is {genre}")
     #counter += 1
     #print(f"{track_message} {counter} : {genre}")
     #index += 1
     
# Task 3

for index in range(len(genres)):
   
        if genres[index] == "Classical":
            continue     
 #       else:
 #           for genre in genres[index]:
        track_counter += 1    
    
        print(f"{track_message} {track_counter} : {genres[index]} is ready for the light show")
        
   
