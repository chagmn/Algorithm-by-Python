//
//  main.swift
//  가운데 글자 가져오기
//
//  Created by 창민 on 2021/07/04.
//

import Foundation

func solution(_ s:String) -> String {
    if s.count%2 == 0 {
        return String(Array(s)[s.count/2-1...s.count/2])
    }
    return String(Array(s)[s.count/2])
}

var s: String = "abcde"
print(solution(s))
