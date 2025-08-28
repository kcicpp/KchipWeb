@extends('layouts.app')

@section('title', 'Shop')

@section('content')
    <!-- Shop Page -->
    <div id="shop" class="page-content">
        <section class="relative z-10 py-20 px-6">
            <div class="max-w-6xl mx-auto">
                <h2 class="orbitron text-5xl font-bold text-white text-center mb-16">🎼 Cửa Hàng Sheet Nhạc</h2>
                
                <!-- Search Bar -->
                <div class="mb-12 text-center">
                    <input 
                        type="text" 
                        placeholder="Tìm kiếm bài hát..." 
                        class="w-full max-w-lg px-4 py-3 rounded-lg bg-white bg-opacity-20 text-white placeholder-blue-200 border border-white border-opacity-30 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                </div>

                <!-- Categories -->
                <div class="flex flex-wrap justify-center gap-4 mb-12">
                    <button class="bg-white bg-opacity-20 text-white px-6 py-3 rounded-full backdrop-blur-sm hover:bg-opacity-30 transition-all inter">Tất Cả</button>
                    <button class="bg-white bg-opacity-20 text-white px-6 py-3 rounded-full backdrop-blur-sm hover:bg-opacity-30 transition-all inter">Việt Nam</button>
                    <button class="bg-white bg-opacity-20 text-white px-6 py-3 rounded-full backdrop-blur-sm hover:bg-opacity-30 transition-all inter">Nhật Bản</button>
                    <button class="bg-white bg-opacity-20 text-white px-6 py-3 rounded-full backdrop-blur-sm hover:bg-opacity-30 transition-all inter">Hàn Quốc</button>
                    <button class="bg-white bg-opacity-20 text-white px-6 py-3 rounded-full backdrop-blur-sm hover:bg-opacity-30 transition-all inter">Trung Quốc</button>
                    <button class="bg-white bg-opacity-20 text-white px-6 py-3 rounded-full backdrop-blur-sm hover:bg-opacity-30 transition-all inter">US-UK</button>
                </div>

                <!-- Products Grid -->
                <div class="grid md:grid-cols-3 lg:grid-cols-4 gap-6">
                    <!-- Product 1 -->
                    <div class="game-card rounded-xl p-4">
                        <div class="bg-gradient-to-br from-blue-400 to-purple-500 rounded-lg h-32 flex items-center justify-center mb-4">
                            <span class="text-3xl">🎵</span>
                        </div>
                        <h4 class="orbitron font-bold text-white mb-2">Dreams of Light</h4>
                        <p class="inter text-blue-200 text-sm mb-1">Tác giả: Nguyễn Văn A</p>
                        <p class="inter text-blue-200 text-sm mb-3">Người soạn: Trần Văn B</p>
                        <div class="flex justify-between items-center">
                            <span class="orbitron text-yellow-300 font-bold">50.000đ</span>
                            <button class="bg-blue-500 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-600 transition-colors">Mua</button>
                        </div>
                    </div>

                    <!-- Product 2 -->
                    <div class="game-card rounded-xl p-4">
                        <div class="bg-gradient-to-br from-pink-400 to-red-500 rounded-lg h-32 flex items-center justify-center mb-4">
                            <span class="text-3xl">🎶</span>
                        </div>
                        <h4 class="orbitron font-bold text-white mb-2">Aurora Concert</h4>
                        <p class="inter text-blue-200 text-sm mb-1">Tác giả: Yamada Taro</p>
                        <p class="inter text-blue-200 text-sm mb-3">Người soạn: Suzuki Hanako</p>
                        <div class="flex justify-between items-center">
                            <span class="orbitron text-yellow-300 font-bold">75.000đ</span>
                            <button class="bg-blue-500 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-600 transition-colors">Mua</button>
                        </div>
                    </div>

                    <!-- Product 3 -->
                    <div class="game-card rounded-xl p-4">
                        <div class="bg-gradient-to-br from-green-400 to-blue-500 rounded-lg h-32 flex items-center justify-center mb-4">
                            <span class="text-3xl">🎼</span>
                        </div>
                        <h4 class="orbitron font-bold text-white mb-2">Forest Theme</h4>
                        <p class="inter text-blue-200 text-sm mb-1">Tác giả: Kim Min Soo</p>
                        <p class="inter text-blue-200 text-sm mb-3">Người soạn: Park Ji Hoon</p>
                        <div class="flex justify-between items-center">
                            <span class="orbitron text-yellow-300 font-bold">30.000đ</span>
                            <button class="bg-blue-500 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-600 transition-colors">Mua</button>
                        </div>
                    </div>

                    <!-- Product 4 -->
                    <div class="game-card rounded-xl p-4">
                        <div class="bg-gradient-to-br from-yellow-400 to-orange-500 rounded-lg h-32 flex items-center justify-center mb-4">
                            <span class="text-3xl">🎹</span>
                        </div>
                        <h4 class="orbitron font-bold text-white mb-2">Valley Race</h4>
                        <p class="inter text-blue-200 text-sm mb-1">Tác giả: John Smith</p>
                        <p class="inter text-blue-200 text-sm mb-3">Người soạn: Jane Doe</p>
                        <div class="flex justify-between items-center">
                            <span class="orbitron text-yellow-300 font-bold">40.000đ</span>
                            <button class="bg-blue-500 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-600 transition-colors">Mua</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
@endsection