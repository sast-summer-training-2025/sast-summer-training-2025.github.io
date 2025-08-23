## 00：3D图像引擎与Unity

### 课程内容：Unity基础

- Unity是什么
- Unity的界面
- 一起做一个简单的Unity项目
- ref：2024年暑培

### 3D图像引擎

3D图像引擎是一种用于生成、处理和渲染三维图像的计算机软件系统。它们在视频游戏、电影特效、虚拟现实（VR）、增强现实（AR）以及各种模拟和可视化应用中发挥着关键作用。

核心功能：

- 渲染（Rendering）
- 物理引擎（Physics Engine）
- 光照与阴影（Lighting and Shadows）
- 动画（Animation）
- 材质与纹理（Materials and Textures）
- 相机系统（Camera System）

### Unity

Unity是一款由Unity Technologies开发的跨平台游戏引擎。它最初发布于2005年，现已成为开发2D和3D游戏以及交互式内容的热门工具

用Unity开发的知名游戏：绝大部分知名的手游

Why Unity？

- 跨平台支持：Unity支持多个平台，包括Windows、MacOS、Linux、iOS、Android、WebGL、PlayStation、Xbox、Nintendo
- Switch等。这使得开发者可以轻松地将他们的游戏或应用发布到多个平台上。
- 强大的编辑器：Unity的编辑器直观且功能强大，允许开发者可视化地设计和调试游戏场景。编辑器中集成了大量的工具和插件，帮助开发者加快开发进程。
- 资源丰富的资产商店：Unity Asset Store提供了丰富的预制资源，包括模型、材质、动画、音效、插件等，开发者可以购买或免费下载并直接应用到自己的项目中，从而节省开发时间和成本。
- 简单！

------

## 01: GUI界面

Unity拥有图形化界面，方便开发者以高效直观的方式开发软件。然而，繁杂的GUI元素可能会导致无从下手，我们将为大家讲解基本的Unity GUI界面

#### 界面布局

在开始之前，我们先把界面布局调整为“2 Split（双窗口）”模式：

- 点击 Window→Layouts→2 Split

此时界面被分为五个主要区域：

1. Scene 视图：用于放置和编辑游戏对象
2. Game 视图：游戏运行时玩家看到的画面
3. Hierarchy（层级）视图：显示当前场景中所有的游戏对象
4. Project（项目）视图：显示所有可用资产（类似于资源库）
5. Inspector（检视）视图：显示当前选中对象的属性

#### 在三维空间中定位游戏对象

- 启动 Unity。我们先创建一个新项目。
- 点击 File→New Project，命名为如“GUI Tutorial”，点击 Create Project

Unity 会自动导入标准资源（音频、贴图、模型等），完成后你会看到一个新场景，此时场景中只有一个 Main Camera（主摄像机），它出现在 Hierarchy 视图中。

- 如果 Scene 视图中看不到摄像机，点击 Hierarchy 中的 Main Camera，然后把鼠标移入 Scene 视图，按下键盘 F（Frame Select），Scene 视图会自动聚焦到摄像机。

这个方法可用于快速定位任何对象。

- 你也可以直接在 Scene 视图中点击对象，或者在 Hierarchy 中选择对象，两者联动。

#### 创建游戏对象

现在我们来往场景中添加一些对象：

- 选择 GameObject→3D Object→Plane，添加一个地面
- 再选择 GameObject→3D Object→Cube，添加一个立方体
- 选择 GameObject→Light→Point Light，添加一个点光源

#### 在 Scene 视图中导航

你可以通过以下方式从不同角度观察场景中的对象：

| 操作     | 快捷键（Mac）     |
| -------- | ----------------- |
| 旋转视角 | Alt + 左键 / 右键 |
| 平移视角 | 中键              |
| 缩放视角 | Alt + 右键 / 滚轮 |

建议使用三键鼠标。如果使用笔记本：

- 点击左上角的“小手”工具，然后：

| 操作     | 快捷键（Mac）       |
| -------- | ------------------- |
| 旋转视角 | Alt + 左键          |
| 平移视角 | 左键                |
| 缩放视角 | 上下滑动 / 捏合缩放 |

- 试一试这些操作感受一下。

#### 移动游戏对象

你可以通过以下工具来调整对象的位置、旋转和缩放：

1. 移动工具（Move Tool）
   - 键盘按 `W`
   - 选中对象后，会出现三个箭头（红 X、绿 Y、蓝 Z）
   - 拖动箭头即可在该轴上移动对象
   - Inspector 面板中可直接输入 XYZ 数值

也可以先把摄像机调整到合适位置，然后点击 GameObject→Align with View，使对象移动到摄像机所看的位置。

1. 旋转工具（Rotate Tool）
   - 键盘按 `E`
   - 拖动环形旋转工具即可旋转对象

小练习：

- 使用移动工具把 Cube 移出视野，然后在 Hierarchy 中选中它按 `F` 找回；
- 再把它移动回 Plane 附近；
- 把 Point Light 移到 Cube 上方照亮 Plane。

#### Game 视图

Game 视图显示游戏运行时的画面。如果此视图中看不到场景物体，说明摄像机方向不对。

- 点击 Main Camera，观察其黄色锥体（拍摄视野）
- 调整 Scene 视图到你希望摄像机看到的位置
- 选中 Main Camera，选择 GameObject→Align With View
- Game 视图画面应该与 Scene 视图一致

你也可以使用移动、旋转工具手动调整摄像机。

#### 缩放游戏对象

- 选中对象，按 `R` 使用缩放工具（Scale）
- 拖动各轴末端的小方块即可缩放
- Inspector 中也可以输入数值

#### 添加组件（Component）

每个 GameObject 都可以添加各种组件（功能）。在 Inspector 中可看到已有组件（如 Transform、Collider 等）。

我们来尝试添加一个物理刚体：

- 创建一个新的 Cube，命名为 PhysicsCube
- 选中它，点击 Component→Physics→Rigidbody，为其添加刚体组件
- 将 PhysicsCube 移到 Pillar 之上稍微偏一点，如图示

点击 Play，PhysicsCube 应掉落并撞到 Pillar 后落到 Plane 上。

#### 复制（Duplicate）

复制对象是 Unity 中非常高效的功能，复制会完整继承原对象的所有组件和属性。

- 选中 PhysicsCube，按 Command + D（或 Edit→Duplicate）
- 会在 Hierarchy 中看到一个新的 PhysicsCube，它和原来处于同一位置
- 使用 Move 工具将它沿 Y 轴向上移动
- 多复制几次，使场景中有 3 个 PhysicsCube

点击 Play，你会看到它们之间自然发生碰撞与堆叠。

------

## 02：Unity 中的脚本（Script）

在 Unity 中，我们通过编写脚本来自定义游戏对象的行为。脚本本质上是一种 Component（组件），可以挂载到任意 GameObject 上，实现逻辑控制。本节将学习：

- 创建脚本
- 打印调试信息
- 获取并修改其他组件（例如 Rigidbody）
- 向刚体施加力（Force）
- 实现最基础的“物理移动”

#### 创建脚本（Script）

为了让玩家 Player 能动起来，我们需要为其添加一个脚本组件：

1. 在 Hierarchy 中选中 `Player`
2. 点击 Add Component → New Script
3. 命名为 `PlayerMovement`，选择语言 C#
4. 点击 Create and Add

说明：

- 新脚本会同时作为组件挂在 Player 上
- Project 面板中也会生成 `.cs` 文件，可拖拽到其他对象重复使用
- 如挂载错误 → 右键脚本组件 → Remove Component 移除

#### 脚本结构与生命周期

双击 `PlayerMovement.cs`，在 IDE 中会看到如下默认结构：

```
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    void Start()
    {
    }

    void Update()
    {
    }
}
```

- `Start()`：在游戏开始时自动调用一次（适合初始化）
- `Update()`：每一帧都会执行（适合主循环逻辑）

在 `Start()` 中添加输出测试：

```
void Start()
{
    Debug.Log("Hello World");
}
```

> `Debug.Log()` 向 Console 输出调试信息
> 必须以 `;` 结尾，大小写敏感

保存 (`Ctrl+S`) → 返回 Unity → 点击 `Play` → `Window→Console` 查看输出。

------

#### 获取组件引用：控制 Rigidbody

我们希望通过脚本控制物理行为，第一步获取刚体组件：

```
public Rigidbody rb;
```

将这行加入类中（通常写在 Start 之上）。保存后回到 Unity，Inspector 中出现 `Rb` 槽位 → 拖拽 Player 身上的 Rigidbody 到此，即完成绑定。

例如：关闭重力：

```
void Start()
{
    rb.useGravity = false;
}
```

运行后刚体会悬空不再下落。

------

#### AddForce：施加物理力

向前施加一个瞬时力：

```
rb.AddForce(0, 200, 500);
```

- 参数分别代表 `(x, y, z)` 三个方向的力
- 写在 `Start()` 中 → 游戏开始时被推一下

------

#### 持续移动：Update + AddForce

```
void Update()
{
    rb.AddForce(0, 0, 200);
}
```

> 问题：不同帧率的电脑速度不同，为了统一运动速度，乘上 `Time.deltaTime`：

```
rb.AddForce(0, 0, 200 * Time.deltaTime);
```

#### 推荐：使用 FixedUpdate() 做物理更新

Unity 推荐物理操作放在 FixedUpdate() 中执行（时间间隔固定）：

```
void FixedUpdate()
{
    rb.AddForce(0, 0, 200 * Time.deltaTime);
}
```

## 03：实战——实现简单移动

我们将使用先前学到的方法，实现一个可以按键左右/前后移动的游戏对象

#### 控制物理效果：Physics 材质

材质是决定一个游戏对象的物理、光学属性的结构化文件，可以指定材料的贴图、摩擦力、反照度等一系列参数

之前，Cube 被 `AddForce()` 推动后经常会旋转跳动、不停翻滚。原因是它与地面之间存在摩擦力。为此我们自定义一个摩擦为 0 的材质：

- Project 面板 → 右键 → `Create > Physic Material`，命名 `Slippery`
- 将 Dynamic Friction 和 Static Friction 改为 0
- 拖拽到地面（Plane）的 BoxCollider → Material 上

此时立方体会在地面上顺滑滑动，但仍可旋转碰撞，画面更自然。

#### 用Inspector变量控制参数，实现快捷调节

现在脚本中移动力是写死的：

```
rb.AddForce(0, 0, 2000 * Time.deltaTime);
```

在Unity中，任何public变量的值都会在inspector中同步显示。因此，我们希望直接在 Inspector 中调节力的大小，只需将希望调节的量写成public变量即可

```
public float forwardForce = 2000f;
```

然后替换原来写死的数字：

```
rb.AddForce(0, 0, forwardForce * Time.deltaTime);
```

#### 使用 if 与 Input 检测玩家按键

检测是否按下某个键 → 使用 `Input.GetKey("键名")`：

```
if (Input.GetKey("d"))
{
    rb.AddForce(sidewaysForce * Time.deltaTime, 0, 0);
}
```

加上反方向：

```
if (Input.GetKey("a"))
{
    rb.AddForce(-sidewaysForce * Time.deltaTime, 0, 0);
}
```

#### 最终脚本示例：PlayerMovement.cs

```
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public Rigidbody rb;

    // 可在 Inspector 中调节
    public float forwardForce = 2000f;
    public float sidewaysForce = 500f;

    // 固定时间步执行 → 用于物理代码
    void FixedUpdate()
    {
        // 向前增加一个持续力
        rb.AddForce(0, 0, forwardForce * Time.deltaTime);

        // 按 D 键 → 向右
        if (Input.GetKey("d"))
        {
            rb.AddForce(sidewaysForce * Time.deltaTime, 0, 0);
        }

        // 按 A 键 → 向左
        if (Input.GetKey("a"))
        {
            rb.AddForce(-sidewaysForce * Time.deltaTime, 0, 0);
        }
    }
}
```

#### 扩展说明

| 点位               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| FixedUpdate()      | 专门用于物理运算，比 `Update()` 调用频率稳定                 |
| Time.deltaTime     | 上一帧到这一帧的时间间隔，用来保持不同电脑上的速度一致       |
| Inspector 中的变量 | 勾选脚本后可实时拖动调整 `forwardForce` 与 `sidewaysForce`   |
| Input 建议优化     | 初学可直接用 `GetKey()`，进阶可用 `Input System` 或 `GetAxis()` |

## 04：实现相机控制

在游戏中，摄像机跟随玩家是最基础却最重要的功能之一。本节我们将通过脚本实现一个“平滑跟随”的第三人称摄像机效果。

#### 错误方式：直接将摄像机作为玩家子物体

虽然可以将 `Main Camera` 拖入 `Player` 对象下作为子节点（Parenting），实现跟随，但问题是：

- 玩家旋转 → 摄像机会一起旋转
- 撞击导致玩家翻滚 → 摄像机也跟着乱转
- 很容易让画面失控

因此不建议这样做。

#### 正确方式：摄像机使用脚本每帧跟随玩家位置

步骤一：添加跟随脚本

- 选中 `Main Camera`
- 点击 Add Component → New Script
- 命名为 `FollowPlayer`，语言 `C#`
- 点击 Create and Add

#### FollowPlayer.cs 脚本

```
using UnityEngine;

public class FollowPlayer : MonoBehaviour
{
    // 要跟随的对象（玩家）
    public Transform player;

    // 摄像机与玩家之间的偏移（位置差）
    public Vector3 offset;

    void Update()
    {
        // 摄像机的位置 = 玩家位置 + 偏移
        transform.position = player.position + offset;
    }
}
```

> 注意：
> `Transform` 变量可以保存对象的位置、旋转和缩放
> `Vector3` 同时保存 x/y/z 三个浮点数（非常适合用于坐标）

#### 在 Unity 中完成绑定

1. 将脚本挂在摄像机上后，Inspector 中出现两个变量：
   - `Player`（拖拽 Hierarchy 中的 Player 对象到此 slot）
   - `Offset`（默认是 (0,0,0)，待设置）
2. 设置 `Offset`，例如：
   - X = 0　（始终位于玩家正后方）
   - Y = 1　（高一点）
   - Z = -5（往后退一些）

#### 工作原理示意

每一帧执行：

```
transform.position = player.position + offset;
```

即：

- 摄像机的位置 = 玩家当前位置 + 我们设定的偏移量
- 当玩家移动 → 摄像机跟着移动，但不会旋转
- 当玩家翻滚 → 摄像机保持稳定、不会跟着滚动

## 05：碰撞检测

在游戏中，我们常常需要让“玩家碰到某物”后触发事件，比如：死亡、扣血、结束游戏等。我们将介绍如何通过 Unity 的物理系统实现碰撞检测（Collision）与事件触发。

#### 添加一个碰撞检测脚本

为避免玩家移动逻辑过于臃肿，我们单独创建一个脚本处理碰撞：

- 选中 `Player`
- Add Component → New Script，命名：`PlayerCollision`，语言 C#
- 打开脚本，清空多余内容，仅保留：

```
using UnityEngine;

public class PlayerCollision : MonoBehaviour
{
    void OnCollisionEnter(Collision collisionInfo)
    {
        Debug.Log(collisionInfo.collider.name);
    }
}
```

解释：

| 函数                      | 说明                                                     |
| ------------------------- | -------------------------------------------------------- |
| `OnCollisionEnter()`      | Unity 内置回调，当本物体与其他碰撞体发生接触时自动调用   |
| `Collision collisionInfo` | 参数中包含本次碰撞的详细信息（接触点、碰撞对象、冲量等） |
| `collisionInfo.collider`  | 获取被碰撞的对象的 Collider                              |
| `.name`                   | 该 Collider 所在 GameObject 的名称                       |

> ⚠ 注意大小写必须严格一致，否则 Unity 不会报错，但函数不会被调用！

#### 构建一个障碍物（Obstacle）

在 Hierarchy 中创建：

- 右键 → 3D Object → Cube → 命名 `Obstacle`
- 添加刚体：Add Component → Rigidbody
- 调节位置、缩放，如：

| Position | Scale        |
| -------- | ------------ |
| y = 1    | x=2, y=1,z=2 |

自定义一个材质使其更明显：

- Project 右键 → Create → Material，命名 `ObstacleMat`
- 修改颜色，拖拽给 `Obstacle`

#### 判断“撞到的是不是障碍物”

简单做法是判断 `name`：

```
if (collisionInfo.collider.name == "Obstacle")
{
    Debug.Log("Hit an obstacle!");
}
```

但这在大规模场景中不可靠（重命名导致失效、性能较差）。

> ✅ 推荐方式：通过 Tag 做类型判定。

#### 使用 Tag 区分物体种类

- 在 `Obstacle` Inspector 中 → Tag → Add Tag → 新建 “Obstacle”
- 再次选择物体 → 将 Tag 设置为 Obstacle

修改脚本：

```
void OnCollisionEnter(Collision collisionInfo)
{
    if (collisionInfo.collider.tag == "Obstacle")
    {
        Debug.Log("Hit an obstacle!");
    }
}
```

#### 撞到后禁用玩家移动脚本

我们希望玩家撞到障碍后立即停止移动，只需拿到 `PlayerMovement` 脚本引用，并设置 `enabled = false`。

```
public class PlayerCollision : MonoBehaviour
{
    public PlayerMovement movement;

    void OnCollisionEnter(Collision collisionInfo)
    {
        if (collisionInfo.collider.tag == "Obstacle")
        {
            movement.enabled = false;
        }
    }
}
```

> 注意：变量 `movement` 暴露为 public，这样我们可以从 Inspector 中拖拽 `PlayerMovement` 上去完成绑定。

#### 最终 PlayerCollision.cs 脚本

```
using UnityEngine;

public class PlayerCollision : MonoBehaviour
{
    // 引用玩家移动脚本
    public PlayerMovement movement;

    // 碰撞回调
    void OnCollisionEnter(Collision collisionInfo)
    {
        // 如果碰到的是带Obstacle标签的物体
        if (collisionInfo.collider.tag == "Obstacle")
        {
            movement.enabled = false;  // 禁用移动
        }
    }
}
```

## 06：构建场景

到目前为止，我们已经拥有：可移动玩家+跟随摄像机+碰撞检测。我们将正式动手做一段“真正的关卡”，并学习如何利用 Prefab 构建工具流、调整移动手感、添加雾效营造氛围。

#### 将障碍物转为 Prefab

Prefab 是 Unity 中的「模版系统」，可在场景中重复使用相同对象，且统一维护属性：

- 将 Hierarchy 中的 `Obstacle` 拖入 Project 面板 → 自动生成 prefab
- 在场景中通过拖拽 Prefab即可实例多个障碍物
- Prefab 的属性可自动同步：修改任意实例 → Inspector → 点击 Apply 即可更新所有实例

Prefab 能大幅提升我们「快速搭建关卡」的效率。

#### 扩展地面，铺出跑道

为了避免玩家走着走着掉下去，我们将 Plane 缩放成长条地面，并向前移动：

| 属性       | 数值  |
| ---------- | ----- |
| Scale Z    | 10000 |
| Position Z | ~4980 |

当然更专业的 endless-runner 通常做法是「移动世界，不移动玩家」，不过我们将继续保持物理真实移动玩家的设计。

#### 建议视角设置（便于搭建）

| 操作                       | 效果                         |
| -------------------------- | ---------------------------- |
| 单击“Y”轴                  | 切换顶视图（正交2D效果）     |
| 单击小立方体               | 切换 Perspective / Isometric |
| Scene 左上 Layers 锁定地面 | 避免误选地面                 |

> 小技巧：Edit → Snap Settings → 设置移动网格（例：X/Y/Z 都为2），然后按住 Ctrl 拖拽 → 精确对齐

#### 快速复制障碍物，搭建 Path

操作姿势：

- 选择 prefab → `Ctrl + D` 复制
- 拖动摆放 → 按住 Ctrl → 启用贴网格移动
- 重复上述过程，设计你自己的挑战路线

> 建议加入各种不同尺寸、朝向与位置的障碍，进一步提升“节奏感”。

#### 调整移动手感：使用 ForceMode.VelocityChange

当前横向移动使用永久 addForce → 手感延迟明显。改为直接设置速度：

```
rb.AddForce(sidewaysForce * Time.deltaTime, 0, 0, ForceMode.VelocityChange);
```

特点：

| ForceMode      | 解释                        |
| -------------- | --------------------------- |
| Force(Default) | 按质量施加连续力 → 有“惯性” |
| VelocityChange | 直接改速度 → 手感灵敏       |

#### 设置 Drag：增加“刹车阻尼”

在 Rigidbody 中：

| 选项 | 建议参数 | 说明             |
| ---- | -------- | ---------------- |
| Drag | 1~2      | 数值越大减速越快 |

适当提高后，玩家换方向时更利落，有“抓地感”。

相应地需要提高移动推力（Forward/SidewaysForce）来维持速度。

#### 添加雾效（Fog）：提升视觉氛围与难度感

操作：

```
Window → Rendering → Lighting → Environment → Fog
```

| 参数      | 推荐       |
| --------- | ---------- |
| Fog Color | 接近背景色 |
| Density   | 0.02~0.05  |

效果：

玩家只能看到前方一小段区域，增强“未知感”，感觉障碍物是渐渐浮现出来的

## 作业

- 查阅资料，通过让player不动，地面移动的方式，实现无限关卡（endless runner）
- 查阅资料，实现菜单、暂停、胜利、失败等UI元素