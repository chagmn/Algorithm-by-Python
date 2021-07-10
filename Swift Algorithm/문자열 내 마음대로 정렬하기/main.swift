//
//  main.swift
//  문자열 내 마음대로 정렬하기
//
//  Created by 창민 on 2021/07/10.
//

import Foundation

func solution(_ strings:[String], _ n:Int) -> [String] {

    return  strings.sorted(by: { Array($0)[n] == Array($1)[n] ? $0 < $1 : Array($0)[n] < Array($1)[n] })
}

var strings = ["abce", "abcd", "cdx"]
var n = 2
print(solution(strings, n))
