Step 1. Create a window    
Step 2. Load background image and draw (in while loop); update screen    
https://www.cnblogs.com/wuzhanpeng/p/4261015.html     

step 3. draw a plane   
load resources for different status of plane; draw plane (in while loop); update screen
place of plane: https://github.com/Kill-Console/PythonShootGame/blob/master/resources/image/shoot.pack   
step 4. control it   
with keyboard keys. Need to consider about not moving outside of screen.   
https://www.cnblogs.com/wuzhanpeng/p/4264267.html     

step 5. optimize main loop    
因为人眼几乎不能分辨出70fps以上的画面，那我们也就没有必要把资源花在无休止地提高刷新率上了       
step 6. pygame sprite   
why? 一个是可以同时控制多个运动的元素，另一个是可以帮我们实现精灵间的碰撞检测      
继承Sprite类编写自己的类；建立精灵组；控制精灵组行为；绘制精灵组成员到screen上   
hero sprite and bullet sprite.   
step 7. shoot the bullet 
Hero类中没有update函数而Bullet类中重写了，这是因为，文档中也说了，update是为了我们方便控制精灵行为的，而Hero的实例只有一个，所以重写update似乎并没有什么必要，而子弹因为有很多，所以我们重写update，方便统一管理      
我们在主循环中使用了ticks来控制射击频率，single_shoot()函数实际就是调用一次，就往子弹组中添加一个子弹精灵，为了避免子弹过于密集，我们需要限制发射子弹的频率       
https://www.cnblogs.com/wuzhanpeng/p/4271312.html    

step 8. draw enemy    
随机是游戏中一个很重要的元素，不可预测的机制为游戏带来了更丰富的体验   
generate enemy: enemy = Enemy(enemy1_surface, [randint(0, SCREEN_WIDTH - enemy1_surface.get_width()), -enemy1_surface.get_height()])     
step 9. collide detection   
判断sprite1.rect与sprite2.rect是否重叠    
这些函数一般是用于检测碰撞的，我们可以大体分为sprite与sprite的碰撞检测，sprite与group的碰撞检测，group与group的碰撞检测。回归问题，子弹是一个group，敌人是一个group    
pygame.sprite.groupcollide()——检测两个group之间所有sprite的碰撞   
groupcollide(group1, group2, dokill1, dokill2, collided = None) -> Sprite_dict    
step 10. 华丽的坠毁    
现在我们已经实现子弹与敌机的碰撞检测了，但凭空消失是在不咋的，我们来一个华丽一点的爆炸！    
导入enemy1爆炸的资源图片；控制爆炸图片切换的速度了，在主循环中加入；当index超出图片下标，判断为爆炸效果演示完毕，销毁坠毁的enemy1精灵    
https://www.cnblogs.com/wuzhanpeng/p/4310450.html    

step 11. Plane player destroy detection   


https://www.cnblogs.com/wuzhanpeng/p/4310312.html   
