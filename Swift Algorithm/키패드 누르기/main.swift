//
//  main.swift
//  키패드 누르기
//
//  Created by 창민 on 2021/07/05.
//

import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    var answer = ""
    var left = 10 // *
    var right = 12 // #
    for i in numbers {
        if i == 1 || i == 4 || i == 7 {
            answer += "L"
            left = i
        } else if i == 3 || i == 6 || i == 9 {
            answer += "R"
            right = i
        } else if i == 2 || i == 5 || i == 8 || i == 0 {
            let zero = i == 0 ? 11 : i
            let leftDistance = abs(zero-left)/3 + abs(zero-left)%3
            let rightDistance = abs(zero-right)/3 + abs(zero-right)%3
            
            if leftDistance == rightDistance {
                if hand == "left" {
                    answer += "L"
                    left = zero
                }else {
                    answer += "R"
                    right = zero
                }
            } else {
                if leftDistance < rightDistance {
                    answer += "L"
                    left = zero
                }else {
                    answer += "R"
                    right = zero
                }
            }
        }
    }
    return answer
}
// LRL (LLR) LL (R) R (L)
var numbers = [1,3,4,5,8,2,1,4,5,9,5]
var hand = "right"

print(solution(numbers, hand))
