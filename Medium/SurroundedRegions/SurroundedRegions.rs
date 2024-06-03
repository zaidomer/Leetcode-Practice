// https://leetcode.com/problems/surrounded-regions/

impl Solution {
    pub fn solve(board: &mut Vec<Vec<char>>) {
        if board.is_empty() {
            return;
        }

        //paths from row edges out
        for col in 0..board[0].len() {
            if board[0][col] == 'O' {
                Self::traverse(board, 0, col);
            }

            if board[board.len() - 1][col] == 'O' {
                Self::traverse(board, board.len() - 1, col);
            }
        }

        //paths from column edges out
        for row in 0..board.len() {
            if board[row][0] == 'O' {
                Self::traverse(board, row, 0);
            }

            if board[row][board[0].len() - 1] == 'O' {
                Self::traverse(board, row, board[0].len() - 1);
            }
        }

        //flip O's and undo visitation markers
        for row in 0..board.len() {
            for col in 0..board[0].len() {
                if board[row][col] == 'O' {
                    board[row][col] = 'X';
                }

                if board[row][col] == 'Y' {
                    board[row][col] = 'O';
                }
            }
        }
    }

    pub fn traverse(board: &mut Vec<Vec<char>>, row: usize, col: usize) {
        if board[row][col] == 'O' {
            board[row][col] = 'Y';
            if row > 0 && board[row - 1][col] == 'O' {
                Self::traverse(board, row - 1, col);
            }

            if col > 0 && board[row][col - 1]  == 'O' {
                Self::traverse(board, row, col - 1);
            }

            if row < board.len() - 1 && board[row + 1][col] == 'O' {
                Self::traverse(board, row + 1, col);
            }

            if col < board[row].len() - 1 && board[row][col + 1] == 'O' {
                Self::traverse(board, row, col + 1);
            }
        }
    }
}