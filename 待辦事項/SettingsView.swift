//
//  SettingsView.swift
//  待辦事項
//
//  Created by yu on 2026/3/15.
//


// SettingsView.swift
import SwiftUI

struct SettingsView: View {
    @AppStorage("colorScheme") private var colorSchemeOption: String = "system"
    @AppStorage("buttonColor") private var buttonColor: String = "blue"

    let colorOptions: [(String, String, Color)] = [
        ("blue",        "藍色（預設）", .blue),
        ("green",       "綠色",         .green),
        ("white",       "白色",         .white),
        ("black",       "黑色",         .black),
        ("purple",      "紫色",         .purple),
    ]

    var body: some View {
        NavigationStack {
            List {
                Section("外觀") {
                    Picker("顯示模式", selection: $colorSchemeOption) {
                        Text("跟隨系統").tag("system")
                        Text("淺色").tag("light")
                        Text("深色").tag("dark")
                    }
                    .pickerStyle(.segmented)
                }

                Section("新增按鈕顏色") {
                    ForEach(colorOptions, id: \.0) { id, label, color in
                        HStack {
                            // 顏色預覽圓圈
                            Circle()
                                .fill(color)
                                .frame(width: 24, height: 24)
                                .overlay(
                                    Circle().stroke(Color.gray.opacity(0.4), lineWidth: 1)
                                )

                            Text(label)

                            Spacer()

                            if buttonColor == id {
                                Image(systemName: "checkmark")
                                    .foregroundColor(.accentColor)
                            }
                        }
                        .contentShape(Rectangle())
                        .onTapGesture {
                            buttonColor = id
                        }
                    }
                }
            }
            .navigationTitle("設定")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}
