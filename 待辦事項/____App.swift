import SwiftUI
import SwiftData
import SwiftUI
import UserNotifications

@main
struct YourAppNameApp: App {
    
    init() {
        // 初始化時請求使用者允許推播通知權限
        UNUserNotificationCenter.current().requestAuthorization(
            options: [.alert, .sound, .badge]
        ) { granted, error in
            if let error = error {
                print("取得通知權限時發生錯誤：\(error.localizedDescription)")
            } else {
                if granted {
                    print("使用者已允許通知")
                } else {
                    print("使用者拒絕通知權限")
                }
            }
        }
        
        // 設定通知的代理人（如需處理通知點擊事件可用）
        UNUserNotificationCenter.current().delegate = NotificationDelegate.shared
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
