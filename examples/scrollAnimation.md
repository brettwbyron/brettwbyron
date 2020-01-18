---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: scrollAnimation
---

<div class="scroll-data flex-row flex-m-space-between flex-c-center">
    Current Scroll Position:<span id="scrollPosition"></span>
</div>

<div class="start-data-ltr">
    <i class="fa fa-arrow-up"></i>Start @ <span id="startPositionLTR"></span>
</div>

<div class="end-data-ltr">
    <i class="fa fa-arrow-up"></i>End @ <span id="endPositionLTR"></span>
</div>

<div class="start-data-rtl">
    <i class="fa fa-arrow-up"></i>Start @ <span id="startPositionRTL"></span>
</div>

<div class="end-data-rtl">
    <i class="fa fa-arrow-up"></i>End @ <span id="endPositionRTL"></span>
</div>

<div id="scrollAnimationLTR">
    <h1>Scrolling Animation (Left to Right)</h1>
    <div class="content">
        <p>This example shows a scroll animation where when scrolling vertically along a page, an element moves horizontally. To do this, we calculate a value depending on where the current scroll position is, where the element is on the page, and where you want your animation to start/stop.</p>
        <p>The current scroll position and element position values you can pull from the page itself, but the most important values are something we need to set ourselves or calculate with an equation. We will use these values to set the moving element's position.</p>
        <p>The ratio represents how far to move the element. <code>0</code> means it's at the starting position and <code>1</code> means it's at the end position. So, <code>0.5</code>, for example, means it's halfway between start and end positions.</p>
        <p>This ratio is calculated using the values of the current scroll position (<code>sp</code>), the position of the element (<code>top</code>), and the point at which you want the animation to start (<code>start</code>).</p>
        <p class="mb0">This is the equation we use:</p>
        <p><code>ratio = (sp - start) / (top - start)</code></p>
        <p>With the value <code>ratio</code>, we turn that into a percentage value by multiplying it by <code>100</code>. So, <code>0.75</code> ends up being <code>(0.75 * 100) = 75%</code></p>
    </div>
    <div class="mask-data">
        <p class="mb0">This is a live version of the above equation:</p>
        <p><code><span id="maskData">ratio = ( 101 - 120 ) / ( 682 - 120 ) = 0</span></code></p>
    </div>
    <div class="scroll-animation">
        <div class="content flex-row flex-c-center flex-m-space-between">
            <div class="position-data">Top Position: <span id="topPosition">682</span></div>
            <div class="column u-text-center flex-col flex-m-center">
                <h2>Static Content</h2>
            </div>
            <div class="column u-text-center flex-col flex-m-center">
                <div id="mask" style="left: 0%;">
                    <div class="left-data">
                        Left: <span id="leftData">0%</span> <i class="fa fa-arrow-right"></i>
                    </div>
                    <h2>This moves</h2>
                </div>
                <h2>This doesn't</h2>
            </div>
        </div>
    </div>
</div>

<div id="scrollAnimationRTL">
    <h1>Scrolling Animation (Right to Left)</h1>
    <div class="mask-data">
        <p>To make the slide go right to left, all you'll need to do is switch the attributes around.</p>
        <p>ratio = (sp - start) / (top - start)</p>
        <p class="mb0">This is a live version of the above equation:</p>
        <p><code><span id="maskData">ratio = ( 101 - 1065 ) / ( 1603 - 1065 ) = 0</span></code></p>
    </div>
    <div class="scroll-animation">
        <div class="content flex-row flex-c-center flex-m-space-between">
            <div class="position-data">Top Position: <span id="topPosition">1603</span></div>
            <div class="column u-text-center flex-col flex-m-center">
                <div id="mask" style="right: 0%;">
                    <div class="right-data">
                        <i class="fa fa-arrow-left"></i> Right: <span id="rightData">0%</span>
                    </div>
                    <h2>This moves</h2>
                </div>
                <h2>This doesn't</h2>
            </div>
            <div class="column u-text-center flex-col flex-m-center">
                <h2>Static Content</h2>
            </div>
        </div>
    </div>
</div>