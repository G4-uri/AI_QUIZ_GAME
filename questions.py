QUESTIONS = [
# ---------------- Foundations and Applications of AI ----------------
{
"id": 1, "type": "MCQ", "difficulty": "Easy", "topic": "Foundations of AI",
"question": "Which definition best describes Artificial Intelligence?",
"options": [
"A system that only follows fixed if-else rules",
"A system that performs tasks requiring human-like intelligence",
"A system that stores data without reasoning",
"A system used only for robotics"
],
"answer": 1,
"explanation": "AI systems perceive, reason, learn, plan, or act intelligently to achieve goals."
},

{
"id": 2, "type": "True/False", "difficulty": "Easy", "topic": "Applications of AI",
"question": "Speech recognition, recommendation systems, and autonomous vehicles are examples of real-world AI applications.",
"options": ["True", "False"],
"answer": 0,
"explanation": "All three use AI techniques such as machine learning, computer vision, planning, and decision-making."
},

{
"id": 3, "type": "MCQ", "difficulty": "Easy", "topic": "Turing Test",
"question": "The Turing Test evaluates whether a machine can:",
"options": [
"Perform arithmetic faster than a human",
"Exhibit conversational behaviour indistinguishable from a human",
"Store unlimited data",
"Run without electricity"
],
"answer": 1,
"explanation": "In the Turing Test, a human judge interacts with a machine and a human; if the judge cannot reliably distinguish them, the machine is said to exhibit intelligent behaviour."
},

{
"id": 4, "type": "Assertion-Reason", "difficulty": "Medium", "topic": "Turing Test",
"question": "Assertion (A): Passing the Turing Test proves that an AI system understands language exactly like humans.\nReason (R): The Turing Test measures behavioural indistinguishability in conversation.",
"options": [
"Both A and R are true, and R explains A",
"Both A and R are true, but R does not explain A",
"A is true, but R is false",
"A is false, but R is true"
],
"answer": 3,
"explanation": "The Turing Test assesses conversational behaviour, not whether the system truly understands language in the human cognitive sense."
},

{
"id": 5, "type": "Fill in the Blank", "difficulty": "Easy", "topic": "Foundations of AI",
"question": "The ability of an AI system to improve performance from experience is called ______.",
"options": ["Learning", "Searching", "Encoding", "Compiling"],
"answer": 0,
"explanation": "Machine learning enables systems to improve from data or experience."
},

{
"id": 6, "type": "MCQ", "difficulty": "Medium", "topic": "Applications of AI",
"question": "A hospital uses an AI model to prioritize X-ray reports based on suspected abnormalities. Which AI application area is primarily used?",
"options": [
"Computer vision",
"Natural language generation",
"Robot locomotion",
"Database normalization"
],
"answer": 0,
"explanation": "Analysing medical images is a computer-vision application."
},

{
"id": 7, "type": "Scenario", "difficulty": "Medium", "topic": "Applications of AI",
"question": "An e-commerce platform recommends products using a customer’s browsing history, purchase history, and similar users’ behaviour. Which AI application is this?",
"options": [
"Recommendation system",
"Optical character recognition",
"Speech synthesis",
"Path planning"
],
"answer": 0,
"explanation": "This is a recommendation system, commonly built using collaborative filtering and machine learning."
},

{
"id": 8, "type": "True/False", "difficulty": "Easy", "topic": "Foundations of AI",
"question": "AI can only be implemented using robots.",
"options": ["True", "False"],
"answer": 1,
"explanation": "AI can be implemented in software systems, web applications, mobile apps, cloud services, and robots."
},

{
"id": 9, "type": "MCQ", "difficulty": "Medium", "topic": "Turing Test",
"question": "In Turing’s imitation game, the judge communicates with participants:",
"options": [
"Only through spoken voice",
"Only through written text",
"Only through facial expressions",
"Only through physical movement"
],
"answer": 1,
"explanation": "The original setup uses text-based communication to avoid bias from voice or appearance."
},

{
"id": 10, "type": "Scenario", "difficulty": "Medium", "topic": "Applications of AI",
"question": "A self-driving car detects pedestrians, traffic lights, lane markings, and nearby vehicles to decide when to brake. Which combination of AI capabilities does this mainly require?",
"options": [
"Computer vision and decision-making",
"Only database management",
"Only text summarization",
"Only password authentication"
],
"answer": 0,
"explanation": "The car uses perception through computer vision and decision-making for safe driving actions."
},

# ---------------- Agents and Environments ----------------
{
"id": 11, "type": "MCQ", "difficulty": "Easy", "topic": "Rational Agents",
"question": "A rational agent is one that:",
"options": [
"Always chooses a random action",
"Selects actions expected to maximize its performance measure",
"Never makes mistakes",
"Only works in fully observable environments"
],
"answer": 1,
"explanation": "Rationality means selecting actions expected to maximize a performance measure, given the agent’s percept sequence and built-in knowledge."
},

{
"id": 12, "type": "True/False", "difficulty": "Easy", "topic": "Intelligent Agents",
"question": "An agent perceives its environment through sensors and acts upon it through actuators.",
"options": ["True", "False"],
"answer": 0,
"explanation": "This is the standard agent architecture: percepts through sensors, actions through actuators."
},

{
"id": 13, "type": "MCQ", "difficulty": "Easy", "topic": "Agents and Environments",
"question": "Which of the following is NOT an agent?",
"options": [
"A thermostat controlling room temperature",
"A chess-playing program",
"A self-driving car",
"A passive text file stored on a disk"
],
"answer": 3,
"explanation": "A passive file does not perceive or act autonomously."
},

{
"id": 14, "type": "Match the Following", "difficulty": "Medium", "topic": "Agents and Environments",
"question": "Match the agent type with its behaviour:\n1. Simple reflex agent\n2. Model-based reflex agent\n3. Goal-based agent\n4. Utility-based agent\n\nA. Uses internal state to handle partial observability\nB. Acts only on the current percept using condition-action rules\nC. Chooses actions that maximize expected happiness/performance\nD. Chooses actions to reach a desired goal state",
"options": [
"1-B, 2-A, 3-D, 4-C",
"1-A, 2-B, 3-C, 4-D",
"1-C, 2-D, 3-A, 4-B",
"1-D, 2-C, 3-B, 4-A"
],
"answer": 0,
"explanation": "Simple reflex agents use current percepts; model-based agents maintain state; goal-based agents plan toward goals; utility-based agents maximize utility."
},

{
"id": 15, "type": "MCQ", "difficulty": "Medium", "topic": "Nature of Environments",
"question": "In a partially observable environment, the agent:",
"options": [
"Has complete access to the entire environment state",
"Cannot access all relevant information about the environment",
"Always knows future states",
"Has no sensors"
],
"answer": 1,
"explanation": "Partial observability means sensors provide incomplete information about the environment."
},

{
"id": 16, "type": "True/False", "difficulty": "Easy", "topic": "Nature of Environments",
"question": "A deterministic environment gives the same outcome for the same action performed in the same state.",
"options": ["True", "False"],
"answer": 0,
"explanation": "In a deterministic environment, the next state is fully determined by the current state and action."
},

{
"id": 17, "type": "Scenario", "difficulty": "Medium", "topic": "Nature of Environments",
"question": "A delivery drone operates in changing weather, moving vehicles, and unpredictable pedestrian movement. Its environment is best described as:",
"options": [
"Static and deterministic",
"Dynamic and stochastic",
"Single-agent and fully observable",
"Discrete and known"
],
"answer": 1,
"explanation": "The environment changes independently of the drone and includes uncertainty, making it dynamic and stochastic."
},

{
"id": 18, "type": "MCQ", "difficulty": "Medium", "topic": "Good Behaviour",
"question": "Which factor is most important when designing a rational agent?",
"options": [
"The number of lines of code",
"The performance measure",
"The colour of the user interface",
"The programming language only"
],
"answer": 1,
"explanation": "The performance measure defines what counts as good behaviour and guides rational action selection."
},

{
"id": 19, "type": "Assertion-Reason", "difficulty": "Medium", "topic": "Rational Agents",
"question": "Assertion (A): A vacuum-cleaner agent that cleans only when it detects dirt can be rational.\nReason (R): Rationality depends on the performance measure, environment, actuators, and percept sequence.",
"options": [
"Both A and R are true, and R explains A",
"Both A and R are true, but R does not explain A",
"A is true, but R is false",
"A is false, but R is true"
],
"answer": 0,
"explanation": "A simple reflex vacuum agent can be rational if its actions maximize cleanliness and minimize cost in its environment."
},

{
"id": 20, "type": "Fill in the Blank", "difficulty": "Easy", "topic": "Agents and Environments",
"question": "The sequence of inputs an agent receives from its environment is called a ______ sequence.",
"options": ["Percept", "Action", "State", "Goal"],
"answer": 0,
"explanation": "A percept is the agent’s input at a given instant; the percept sequence is the complete history of inputs."
},

# ---------------- Problem Solving and Search ----------------
{
"id": 21, "type": "MCQ", "difficulty": "Easy", "topic": "Problems and Problem Spaces",
"question": "Which of the following is NOT a standard component of a well-defined search problem?",
"options": [
"Initial state",
"Actions",
"Transition model",
"Compiler version"
],
"answer": 3,
"explanation": "A search problem includes initial state, actions, transition model, goal test, and path-cost function."
},

{
"id": 22, "type": "True/False", "difficulty": "Easy", "topic": "State Space Search",
"question": "A state space is the set of all possible states reachable from the initial state through valid actions.",
"options": ["True", "False"],
"answer": 0,
"explanation": "The state space represents possible configurations and transitions in a problem."
},

{
"id": 23, "type": "MCQ", "difficulty": "Medium", "topic": "Production Systems",
"question": "A production system mainly consists of:",
"options": [
"A set of rules, working memory, and a control strategy",
"Only a database",
"Only a neural network",
"Only a user interface"
],
"answer": 0,
"explanation": "Production systems use rules, a working memory or database, and a control strategy to select applicable rules."
},

{
"id": 24, "type": "Fill in the Blank", "difficulty": "Easy", "topic": "Production Systems",
"question": "In a production system, a rule has the form: IF condition THEN ______.",
"options": ["Action", "Compiler", "Dataset", "Interface"],
"answer": 0,
"explanation": "Production rules map conditions in working memory to actions or new facts."
},

{
"id": 25, "type": "MCQ", "difficulty": "Medium", "topic": "Problem Characteristics",
"question": "Which problem characteristic asks whether the solution is a path or simply a final state?",
"options": [
"Is the problem decomposable?",
"Can the solution be a path or a state?",
"Is the environment observable?",
"Is the heuristic admissible?"
],
"answer": 1,
"explanation": "Some problems require the entire solution path, such as route finding, while others require only a final state, such as a solved puzzle."
},

{
"id": 26, "type": "MCQ", "difficulty": "Medium", "topic": "Issues in Search Program Design",
"question": "Which issue is most important when selecting a search algorithm for a very large state space?",
"options": [
"Time and memory requirements",
"Font size of the program",
"Number of comments in code",
"Screen resolution"
],
"answer": 0,
"explanation": "Search algorithms must balance computational time, memory usage, completeness, and optimality."
},

{
"id": 27, "type": "Problem Solving", "difficulty": "Medium", "topic": "BFS",
"question": "In BFS, which data structure is used to manage the frontier?",
"options": [
"Stack",
"Queue",
"Priority queue",
"Hash table"
],
"answer": 1,
"explanation": "BFS uses a FIFO queue, expanding shallowest unexpanded nodes first."
},

{
"id": 28, "type": "Problem Solving", "difficulty": "Medium", "topic": "DFS",
"question": "In DFS, which data structure is typically used to manage exploration?",
"options": [
"Queue",
"Stack",
"Set only",
"Linked list only"
],
"answer": 1,
"explanation": "DFS uses LIFO behaviour, commonly implemented through recursion or an explicit stack."
},

{
"id": 29, "type": "Problem Solving", "difficulty": "Hard", "topic": "BFS",
"question": "A graph has start node S connected to A and B. A connects to C. B connects to D. C and D connect to goal G. Using BFS, which node is expanded immediately after S?",
"options": [
"G",
"A and B",
"C and D",
"Only G"
],
"answer": 1,
"explanation": "BFS expands all nodes at depth 1 before moving to depth 2, so A and B are expanded after S."
},

{
"id": 30, "type": "Problem Solving", "difficulty": "Hard", "topic": "BFS",
"question": "In an unweighted graph, BFS is guaranteed to find:",
"options": [
"The path with the fewest edges to the goal",
"The deepest path",
"A random path",
"The path with maximum cost"
],
"answer": 0,
"explanation": "BFS explores level by level, so in an unweighted graph it finds a solution with the minimum number of edges."
},

{
"id": 31, "type": "True/False", "difficulty": "Medium", "topic": "DFS",
"question": "DFS always finds the shortest path in an unweighted graph.",
"options": ["True", "False"],
"answer": 1,
"explanation": "DFS may find a longer path first because it explores deeply before considering other branches."
},

{
"id": 32, "type": "MCQ", "difficulty": "Medium", "topic": "Iterative Deepening",
"question": "Iterative deepening search combines the advantages of:",
"options": [
"BFS and DFS",
"Hill climbing and CSP",
"Means-end analysis and production systems",
"Supervised and unsupervised learning"
],
"answer": 0,
"explanation": "Iterative deepening repeatedly performs depth-limited DFS with increasing limits, giving BFS-like completeness with DFS-like memory use."
},

{
"id": 33, "type": "Problem Solving", "difficulty": "Hard", "topic": "Iterative Deepening",
"question": "If the goal is at depth 3 and iterative deepening uses depth limits 0, 1, 2, and 3, at which iteration will it first find the goal?",
"options": [
"Depth limit 0",
"Depth limit 1",
"Depth limit 2",
"Depth limit 3"
],
"answer": 3,
"explanation": "A depth-limited search cannot reach a node deeper than its limit, so the goal at depth 3 is found when the limit is 3."
},

{
"id": 34, "type": "MCQ", "difficulty": "Medium", "topic": "Hill Climbing",
"question": "Hill climbing is a:",
"options": [
"Local search algorithm",
"Unsupervised learning algorithm",
"Database indexing method",
"Network protocol"
],
"answer": 0,
"explanation": "Hill climbing repeatedly moves to a neighbouring state with a better heuristic value."
},

{
"id": 35, "type": "MCQ", "difficulty": "Hard", "topic": "Hill Climbing",
"question": "A hill-climbing algorithm reaches a state where no neighbouring state has a better value, but the global optimum is elsewhere. This is called:",
"options": [
"Local maximum",
"Global maximum",
"Plateau",
"Ridge"
],
"answer": 0,
"explanation": "A local maximum is a state better than all its neighbours but worse than the global optimum."
},

{
"id": 36, "type": "Match the Following", "difficulty": "Hard", "topic": "Hill Climbing Variations",
"question": "Match the hill-climbing variation with its main idea:\n1. Simple hill climbing\n2. Steepest-ascent hill climbing\n3. Stochastic hill climbing\n4. Random-restart hill climbing\n\nA. Chooses randomly among improving moves\nB. Evaluates all neighbours and chooses the best\nC. Restarts from different initial states\nD. Chooses the first improving neighbour",
"options": [
"1-D, 2-B, 3-A, 4-C",
"1-A, 2-D, 3-B, 4-C",
"1-C, 2-A, 3-D, 4-B",
"1-B, 2-C, 3-D, 4-A"
],
"answer": 0,
"explanation": "Simple hill climbing takes the first improvement; steepest ascent evaluates all neighbours; stochastic chooses randomly among improvements; random restart reduces local-maxima problems."
},

{
"id": 37, "type": "Scenario", "difficulty": "Hard", "topic": "Hill Climbing",
"question": "A delivery company uses hill climbing to optimize delivery routes. The algorithm repeatedly gets stuck at the same non-optimal route. Which variation would most directly help?",
"options": [
"Random-restart hill climbing",
"Breadth-first search",
"Linear regression",
"Binary search"
],
"answer": 0,
"explanation": "Random restarts begin from multiple initial solutions, increasing the chance of escaping local optima."
},

{
"id": 38, "type": "MCQ", "difficulty": "Medium", "topic": "Heuristic Search",
"question": "A heuristic function is used to:",
"options": [
"Estimate the cost or distance from a state to a goal",
"Store all previous states permanently",
"Remove all uncertainty from a problem",
"Replace the goal test"
],
"answer": 0,
"explanation": "Heuristics guide informed search by estimating closeness to the goal."
},

{
"id": 39, "type": "MCQ", "difficulty": "Hard", "topic": "Best First Search",
"question": "Greedy best-first search expands the node with the lowest:",
"options": [
"Path cost from start, g(n)",
"Heuristic estimate to goal, h(n)",
"Total estimated cost, f(n) = g(n) + h(n)",
"Node depth only"
],
"answer": 1,
"explanation": "Greedy best-first search uses only the heuristic estimate h(n), which can be fast but is not guaranteed optimal."
},

{
"id": 40, "type": "True/False", "difficulty": "Hard", "topic": "Heuristic Search",
"question": "A heuristic is admissible if it never overestimates the true cost to reach the goal.",
"options": ["True", "False"],
"answer": 0,
"explanation": "An admissible heuristic is optimistic; it never overestimates the remaining cost."
},

{
"id": 41, "type": "Problem Solving", "difficulty": "Hard", "topic": "Best First Search",
"question": "At a search frontier, nodes have heuristic values A = 8, B = 3, C = 6. Greedy best-first search expands:",
"options": [
"A",
"B",
"C",
"Any node randomly"
],
"answer": 1,
"explanation": "Greedy best-first search selects the node with the smallest heuristic value, which is B = 3."
},

# ---------------- CSP and Means-End Analysis ----------------
{
"id": 42, "type": "MCQ", "difficulty": "Medium", "topic": "CSP",
"question": "A Constraint Satisfaction Problem consists of:",
"options": [
"Variables, domains, and constraints",
"Only inputs and outputs",
"Only a reward function",
"Only a neural network"
],
"answer": 0,
"explanation": "A CSP assigns values to variables from their domains while satisfying all constraints."
},

{
"id": 43, "type": "Scenario", "difficulty": "Hard", "topic": "CSP",
"question": "A university must timetable classes so that no teacher or classroom is assigned to two classes at the same time. This is best modelled as:",
"options": [
"A constraint satisfaction problem",
"A linear regression problem",
"A clustering problem",
"A speech recognition problem"
],
"answer": 0,
"explanation": "Timetabling has variables such as classes, domains such as time slots, and constraints such as no teacher or room clashes."
},

{
"id": 44, "type": "Problem Solving", "difficulty": "Hard", "topic": "CSP",
"question": "In map colouring, three regions A, B, and C are pairwise adjacent. Only two colours, Red and Blue, are available. How many valid colour assignments exist?",
"options": [
"0",
"2",
"4",
"6"
],
"answer": 0,
"explanation": "Three mutually adjacent regions require three different colours, but only two colours are available, so no valid assignment exists."
},

{
"id": 45, "type": "MCQ", "difficulty": "Medium", "topic": "CSP",
"question": "Which technique assigns a value, checks constraints, and backtracks when a conflict occurs?",
"options": [
"Backtracking search",
"K-means clustering",
"Gradient descent",
"Principal component analysis"
],
"answer": 0,
"explanation": "Backtracking incrementally builds assignments and undoes choices when constraints are violated."
},

{
"id": 46, "type": "MCQ", "difficulty": "Medium", "topic": "Means-End Analysis",
"question": "Means-end analysis reduces a problem by:",
"options": [
"Identifying differences between current and goal states, then selecting operators to reduce them",
"Trying every possible action randomly",
"Using only supervised learning",
"Ignoring the goal state"
],
"answer": 0,
"explanation": "Means-end analysis compares the current state with the goal and chooses actions that reduce the detected difference."
},

{
"id": 47, "type": "Scenario", "difficulty": "Hard", "topic": "Means-End Analysis",
"question": "A robot must move a block from Table A to Table B, but another block is on top of it. It first removes the upper block, then moves the target block. This is an example of:",
"options": [
"Means-end analysis",
"Supervised classification",
"Image segmentation",
"Database replication"
],
"answer": 0,
"explanation": "The robot identifies an obstacle preventing the goal and applies an operator to reduce that difference."
},

{
"id": 48, "type": "Fill in the Blank", "difficulty": "Easy", "topic": "Means-End Analysis",
"question": "In means-end analysis, the difference between the current state and the desired state is called the ______.",
"options": ["Difference", "Reward", "Loss", "Gradient"],
"answer": 0,
"explanation": "The algorithm identifies differences and selects operators to reduce them."
},

{
"id": 49, "type": "Assertion-Reason", "difficulty": "Hard", "topic": "Search Algorithms",
"question": "Assertion (A): BFS requires more memory than DFS in many large search trees.\nReason (R): BFS stores all nodes at the current frontier level, while DFS stores mainly the current path.",
"options": [
"Both A and R are true, and R explains A",
"Both A and R are true, but R does not explain A",
"A is true, but R is false",
"A is false, but R is true"
],
"answer": 0,
"explanation": "BFS can have exponential memory requirements because it retains a wide frontier, whereas DFS stores the current path and its siblings."
},

{
"id": 50, "type": "Problem Solving", "difficulty": "Hard", "topic": "State Space Search",
"question": "A search tree has branching factor 2 and the goal is at depth 4. What is the maximum number of nodes BFS may need to expand before reaching the goal, assuming no repeated states?",
"options": [
"8",
"15",
"16",
"31"
],
"answer": 3,
"explanation": "The total number of nodes up to depth 4 is 1 + 2 + 4 + 8 + 16 = 31."
}
]