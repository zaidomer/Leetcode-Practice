# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ## VALID TOPOLOGICAL BFS O(V+E) time and space
        # graph = defaultdict(list)
        # numIngredientsNeeded = defaultdict(int)

        # for i in range(len(recipes)):
        #     numIngredientsNeeded[recipes[i]]=len(ingredients[i])
        #     for j in range(len(ingredients[i])):
        #         graph[ingredients[i][j]].append(recipes[i])

        # supplies = set(supplies)
        # q = deque(supplies)
        # res = []

        # while q:
        #     supply = q.popleft()
        #     if supply in numIngredientsNeeded: #can use the map since keys here are recipes
        #         res.append(supply)

        #     for recipe in graph[supply]:
        #         numIngredientsNeeded[recipe]-=1
        #         if numIngredientsNeeded[recipe]==0:
        #             q.append(recipe)
        # return res










        ## VALID TOPOLOGICAL DFS O(V+E) time and space
        food = {}
        for i in range(len(recipes)):
            food[recipes[i]] = ingredients[i]
        res = []
        supplies = set(supplies)
        visit = set()

        def dfs(ingredient):
            if ingredient in supplies:
                return True
            elif ingredient in visit or ingredient not in food:
                return False

            visit.add(ingredient)
            for subIngredient in food[ingredient]:
                if not dfs(subIngredient):
                    return False
            visit.discard(ingredient)
            supplies.add(ingredient)
            return True 

        for recipe in food:
            canMake = True
            for ingredient in food[recipe]:
                if not dfs(ingredient):
                    canMake = False
                    break
            if canMake:
                res.append(recipe)
        return res
