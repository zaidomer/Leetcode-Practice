// https://leetcode.com/problems/rotate-image/description/

class Solution {
public:
    // void rotate(vector<vector<int>>& matrix) {
    //     int diff = matrix.size()-1;
    //     int end = matrix.size();
    //     int start=0;
    //     int row = 0;
    //     int col = 0;
        
    //     for(int i = 0; i < matrix.size()/2; i++){
    //         for(int j = start; j < end-1; j++){
    //             int row = i;
    //             int col = j;
    //             for(int x = 0; x < 3; x++){
    //                 if(x==0){
    //                     int change = diff;
    //                     int newCol=min(col+diff, end-1);
    //                     change-=abs(col-newCol);
    //                     col=newCol;
    //                     row+=change;
    //                 }else if(x==1){
    //                     int change = diff;
    //                     int newRow = min(row+diff, end-1);
    //                     change-=abs(row-newRow);
    //                     row=newRow;
    //                     col-=change;
    //                 }else{
    //                     int change = diff;
    //                     int newCol = max(col-diff,start);
    //                     change-=abs(newCol-col);
    //                     col=newCol;
    //                     row-=change;
    //                 }

    //                 int temp = matrix[row][col];
    //                 matrix[row][col] = matrix[i][j];
    //                 matrix[i][j] = temp;
    //             }
    //         }
    //         diff-=2;
    //         start+=1;
    //         end-=1;
    //     }
    // }

    void swap(int *x, int *y){
        int temp = *x;
        *x = *y;
        *y = temp;
    }

    void printArr(vector<vector<int>> &matrix){
        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < matrix[i].size(); j++){
                std::cout << matrix[i][j] << ", ";
            }
            std::cout<<std::endl;
        }
        std::cout<<std::endl;;
    }

    void rotate(vector<vector<int>> &matrix){
        for(int i = 0; i < matrix.size(); i++){
            for(int j = i+1; j < matrix.size(); j++){
                swap(&matrix[i][j], &matrix[j][i]);
            }
            // printArr(matrix);
        }

        for(int i = 0; i < matrix.size(); i++){
            reverse(matrix[i].begin(), matrix[i].end());    
        }
    }
};

/*
0,0
0,2 -> add col
2,2 -> add row
2,0 -> sub col

0,1
1,2
2,1
1,0



*/
