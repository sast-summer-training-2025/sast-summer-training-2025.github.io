package Answer;

import java.util.Random;
import java.util.Scanner;

class RaceRunner extends Thread {
    private final String name;
    private final RaceRunner nextRunner; // 下一位选手
    private final Random random = new Random();

    @Override
    public String toString() {
        return name;
    }

    public RaceRunner(String name, RaceRunner nextRunner) {
        this.name = name;
        this.nextRunner = nextRunner;
    }

    @Override
    public void run() {
        try {
            System.out.println(name + " started running...");

            // 随机生成 500~1500 毫秒的跑步时间
            int time = 500 + random.nextInt(1000);

            // 模拟跑步
            Thread.sleep(time);

            // 输出完成信息
            System.out.println(name + " finished! Time: " + time + " ms");

            // 如果有下一位选手，则启动并等待其完成
            if (nextRunner != null) {
                System.out.println(name + " passing baton to " + nextRunner);
                nextRunner.start();
                nextRunner.join();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class ThreadRelayRaceAnswer {
    public static void main(String[] args) throws InterruptedException {
        Scanner scanner = new Scanner(System.in);

        // 手动输入选手人数
        System.out.print("Enter number of runners: ");
        int numRunners = scanner.nextInt();

        if (numRunners <= 0) {
            System.out.println("Number of runners must be greater than 0.");
            return;
        }

        // 创建 Runner 数组，并按顺序链接
        RaceRunner[] runners = new RaceRunner[numRunners];
        for (int i = numRunners - 1; i >= 0; i--) {
            RaceRunner next = (i == numRunners - 1) ? null : runners[i + 1];
            runners[i] = new RaceRunner("Runner " + (i + 1), next);
        }

        // 启动第一位 Runner，并等待比赛结束
        runners[0].start();
        runners[0].join();

        System.out.println("Race finished!");
    }
}
