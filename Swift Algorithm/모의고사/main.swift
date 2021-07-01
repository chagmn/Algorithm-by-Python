//
//  main.swift
//  모의고사
//
//  Created by 창민 on 2021/07/01.
//

import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let one = [1,2,3,4,5]
    let two = [2,1,2,3,2,4,2,5]
    let three = [3,3,1,1,2,2,4,4,5,5]
    
    var score = [Int:Int]()
    
    // 채점
    for i in 0..<answers.count {
        if one[i%one.count] == answers[i] {
            score[1] = (score[1] ?? 0) + 1
        }
        if two[i%two.count] == answers[i] {
            score[2] = (score[2] ?? 0) + 1
        }
        if three[i%three.count] == answers[i] {
            score[3] = (score[3] ?? 0) + 1
        }
    }
    return score.filter{$0.value == score.values.max()}.keys.sorted()

}


var answer = [1,3,2,4,2]
print(solution(answer))
