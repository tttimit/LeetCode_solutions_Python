class Solution(object):
    def isValidSudoku(self, board):
        #print(board)
        """
        :type board: List[List[str]]，空格用 . 表示
        :rtype: bool
        """
        # 检查每一行
        for row in board:
            if not self.is_valid_row(row):
                return False

        print("检查每一行没问题")

        # print("{0}x{1}".format(len(board[0]), len(board)))
        # 检查每一列
        for i in range(0, len(board[0])):
            l1 = []
            for j in range(0, len(board)):
                # print("i={0}, j={1}".format(i, j))
                l1.append(board[j][i])
            # print(l1)
            if not self.is_valid_row(l1):
                return False

        print("检查每一列没问题")

        interval = 3

        # 检查每一个方格
        for i in range(1, 8, interval):
            for j in range(1, 8, interval):
                # print("i={0}, j={1}".format(i, j))
                l1 = self.generate_list(board, i, j)
                if not self.is_valid_row(l1):
                    return False
        print("检查每个3x3方格没问题")
        return True

    def is_valid_row(self, row):
        """
        :param row: List[str]
        :return: bool
        """
        if len(row) != 9:
            return False
        checklist = set()
        while '.' in row:
            if isinstance(row, str):
                row = row.replace('.', '')
            elif isinstance(row, list):
                row.remove(".")
        for i in row:
            num = int(i)
            if num > 9 or num < 1:
                print(">9 or <1", num)
                return False
            else:
                if i in checklist:
                    print("repeated:", i)
                    return False
                else:
                    checklist.add(i)
        return True

    def generate_list(self, board, i, j):
        l1 = []
        for a in range(i - 1, i + 2):
            for b in range(j - 1, j + 2):
                l1.append(board[a][b])
        # count = 0
        # for q in l1:
        #     print(q, end=" ")
        #     count += 1
        #     if count == 3:
        #         print()
        #         count = 0
        # print("---")
        return l1


if __name__ == "__main__":
    s = Solution()
    b = [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
         "9........"]
    print(s.isValidSudoku(b))
	
	## new test
	## new test
