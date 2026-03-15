// SettingsView.swift
import SwiftUI

struct SettingsView: View {
    @AppStorage("colorScheme") private var colorSchemeOption: String = "system"

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
            }
            .navigationTitle("設定")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}