# film_renting

Simulation of film renting firm

## Functions:

1. **load_data()**

   - Description: The `load_data` function loads movie and client data from respective JSON files into global variables movies and clients.
   - Arguments: None
   - Returns: None
2. **save_data()**

   - Description: The `save_data` function saves the current state of movie and client data into their respective JSON files.
   - Arguments: None
   - Returns: None
3. **ADD_movie(movie: dict)**

   - Description: The `ADD_movie` function adds a new movie to the global list of movies.
   - Arguments:
     - `movie` (dict): A dictionary representing the details of the movie to be added.
   - Returns: None
4. **DEL_movie(id: int)**

   - Description: The `DEL_movie` function deletes a movie from the global list of movies based on the provided ID.
   - Arguments:
     - `id` (int): The unique identifier of the movie to be deleted.
   - Returns: None
5. **MOD_movie(id: int, movie: dict)**

   - Description: The `MOD_movie` function modifies the details of a movie in the global list based on the provided ID.
   - Arguments:
     - `id` (int): The unique identifier of the movie to be modified.
     - `movie` (dict): A dictionary representing the updated details of the movie.
   - Returns: None
6. **ADD_client(client: dict)**

   - Description: The `ADD_client` function adds a new client to the global list of clients.
   - Arguments:
     - `client` (dict): A dictionary representing the details of the client to be added.
   - Returns: None
7. **DEL_client(id: int)**

   - Description: The `DEL_client` function deletes a client from the global list of clients based on the provided ID.
   - Arguments:
     - `id` (int): The unique identifier of the client to be deleted.
   - Returns: None
8. **MOD_client(id: int, client: dict)**

   - Description: The `MOD_client` function modifies the details of a client in the global list based on the provided ID.
   - Arguments:
     - `id` (int): The unique identifier of the client to be modified.
     - `client` (dict): A dictionary representing the updated details of the client.
   - Returns: None
9. **get_movies()**

   - Description: The `get_movies` function returns a copy of the global list of movies.
   - Arguments: None
   - Returns: A list containing the details of movies.
10. **get_clients()**

- Description: The `get_clients` function returns a copy of the global list of clients.
- Arguments: None
- Returns: A list containing the details of clients.

11. **create_movie(id: int, name: str, description: str, genre: str)**

- Description: The `create_movie` function creates a movie dictionary with the provided details and initializes it with default values ('NaN' for id, name, description, and genre).
- Arguments:
  - `id` (int): The unique identifier for the movie.
  - `name` (str): The name of the movie.
  - `description` (str): A brief description of the movie.
  - `genre` (str): The genre of the movie.
- Returns: A dictionary representing the movie with initialized values.

12. **create_client(id: int, name: str, pid: str)**

- Description: The `create_client` function creates a client dictionary with the provided details and initializes it with default values ('NaN' for id, name, and pid).
- Arguments:
  - `id` (int): The unique identifier for the client.
  - `name` (str): The name of the client.
  - `pid` (str): The personal identification information of the client.
- Returns: A dictionary representing the client with initialized values.

13. **add_movie(name: str, description: str, genre: str)**

- Description: The `add_movie` function adds a new movie to the global list of movies.
- Arguments:
  - `name` (str): The name of the movie.
  - `description` (str): A brief description of the movie.
  - `genre` (str): The genre of the movie.
- Returns: None

14. **del_movie(ids: list)**

- Description: The `del_movie` function deletes movies from the global list based on the provided list of IDs.
- Arguments:
  - `ids` (list): A list of unique identifiers for the movies to be deleted.
- Returns: None

15. **mod_movie(id: int, name: str, description: str, genre: str)**

- Description: The `mod_movie` function modifies the details of a movie in the global list based on the provided ID.
- Arguments:
  - `id` (int): The unique identifier of the movie to be modified.
  - `name` (str): The updated name of the movie.
  - `description` (str): The updated description of the movie.
  - `genre` (str): The updated genre of the movie.
- Returns: None

16. **add_client(name: str, pid: str)**

    - Description: The `add_client` function adds a new client to the global list of clients.
    - Arguments:
      - `name` (str): The name of the client.
      - `pid` (str): The personal identification information of the client.
    - Returns: None
17. **del_client(ids: list)**

    - Description: The `del_client` function deletes clients from the global list based on the provided list of IDs.
    - Arguments:
      - `ids` (list): A list of unique identifiers for the clients to be deleted.
    - Returns: None
18. **mod_client(id: int, name: str, pid: str)**

    - Description: The `mod_client` function modifies the details of a client in the global list based on the provided ID.
    - Arguments:
      - `id` (int): The unique identifier of the client to be modified.
      - `name` (str): The updated name of the client.
      - `pid` (str): The updated personal identification information of the client.
    - Returns: None
19. **get_next_client_id()**

    - Description: The `get_next_client_id` function calculates the next available unique identifier for a client.
    - Arguments: None
    - Returns: An integer representing the next available client ID.
20. **get_next_movie_id()**

    - Description: The `get_next_movie_id` function calculates the next available unique identifier for a movie.
    - Arguments: None
    - Returns: An integer representing the next available movie ID.
21. **search_movie(prop: dict)**

    - Description: The `search_movie` function searches for movies in the global list based on the provided property and value.
    - Arguments:
      - `prop` (dict): A dictionary with 'property' indicating the search property ('id', 'name', 'description', or 'genre') and 'value' indicating the value to search for.
    - Returns: A list of unique identifiers for the matching movies.
22. **search_client(prop: dict)**

    - Description: The `search_client` function searches for clients in the global list based on the provided property and value.
    - Arguments:
      - `prop` (dict): A dictionary with 'property' indicating the search property ('id', 'name', or 'pid') and 'value' indicating the value to search for.
    - Returns: A list of unique identifiers for the matching clients.
23. **load_data_from_file(filename: str)**

    - Description: The `load_data_from_file` function loads data from a JSON file and returns the content as a Python object.
    - Arguments:
      - `filename` (str): The name of the JSON file to load.
    - Returns: A Python object representing the data loaded from the file. If an error occurs during loading, it returns None.
24. **save_data_to_file(data: Any, filename: str)**

    - Description: The `save_data_to_file` function saves data to a JSON file.
    - Arguments:
      - `data` (Any): The Python object to be saved to the file.
      - `filename` (str): The name of the JSON file to which the data will be saved.
    - Returns: None
25. **load()**

    - Description: The `load` function invokes the `load_data` function from the b module, loading movie and client data.
    - Arguments: None
    - Returns: None
26. **save()**

    - Description: The `save` function invokes the `save_data` function from the b module, saving the current state of movie and client data.
    - Arguments: None
    - Returns: None
27. **print_movie(movie: dict)**

    - Description: The `print_movie` function prints the details of a movie dictionary, including its name, description, and genre.
    - Arguments:
      - `movie` (dict): A dictionary representing the details of the movie.
    - Returns: None
28. **print_client(client: dict)**

    - Description: The `print_client` function prints the details of a client dictionary, including its name and personal identification information (PID).
    - Arguments:
      - `client` (dict): A dictionary representing the details of the client.
    - Returns: None
29. **print_movies(ids: list)**

    - Description: The `print_movies` function prints the details of movies based on the provided list of movie IDs.
    - Arguments:
      - `ids` (list): A list of unique identifiers for the movies to be printed. If [-1] is provided, all movies will be printed.
    - Returns: None
30. **print_clients(ids: list)**

    - Description: The `print_clients` function prints the details of clients based on the provided list of client IDs.
    - Arguments:
      - `ids` (list): A list of unique identifiers for the clients to be printed. If [-1] is provided, all clients will be printed.
    - Returns: None
31. **get_confirm()**

    - Description: The `get_confirm` function prompts the user to type "CONFIRM" to confirm a certain operation.
    - Arguments: None
    - Returns: 1 if the user types "CONFIRM," otherwise 0.
32. **read_com()**

    - Description: The `read_com` function reads and interprets user commands for managing clients and movies. It processes commands entered by the user in a loop until the user enters the "exit" command.
    - Arguments: None
    - Returns: None

### Commands:

- `add_c <name> <pid>`: Adds a new client with the specified name and personal identification information (PID).
- `add_m <name> <description> <genre>`: Adds a new movie with the specified name, description, and genre.
- `src_c <property> <value>`: Searches for clients based on the specified property and value.
- `src_m <property> <value>`: Searches for movies based on the specified property and value.
- `del_c <property> <value>`: Deletes clients based on the specified property and value after user confirmation.
- `del_m <property> <value>`: Deletes movies based on the specified property and value after user confirmation.
- `view_c`: Displays a list of all clients.
- `view_m`: Displays a list of all movies.
- `save`: Saves the current state of data.
- `load`: Loads data from files.
- `exit`: Exits the command loop.
- `clearc`: Clears the console screen.

### Note:

- Commands are entered in the format command_descriptor arguments, where the descriptor indicates whether the operation is related to clients (c) or movies (m).
- The function processes multiple commands separated by semicolons (;).
- Invalid descriptors or commands are handled with appropriate error messages.
- The exit command terminates the command loop.
- The clearc command clears the console screen.
- User confirmation is required for deletion operations (del_c and del_m).
- The function provides feedback on the executed commands, such as printing the entries to be deleted and asking for confirmation

### Running scenario:
| User                                                   | Program                   | Description                                             |
|--------------------------------------------------------|---------------------------|---------------------------------------------------------|
|                                                        | Displays prompt           | Awaits user input                                       |
| add_c John Doe,1234321543                              | Displays prompt           | Client John Doe added to the list of client             |
| add_m Darling in the Franxx,Dystopian love anime,Anime | Displays prompt           | Movie Darling in the Franxx added to the list of movies |
| add_r id,1,id,1                                        | Displays prompt           | Assigns the movie with id:1 to the client id:1          |
| del_r id,1                                             | Displays prompt           | Returns the rent with the id:1                          |
| save                                                   | Displays save confirmation| Saves the session                                       |
| exit                                                   |                           | Exits the program                                       |