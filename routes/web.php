<?php
use App\Http\Controllers\Auth\RegisterController;
use Illuminate\Support\Facades\Route;


Route::get('/home', function () {
    return view('home');
});
Route::get('/shop', function () {
    return view('shop');
});
Route::get('/community', function () {
    return view('community');
});
Route::get('/support', function () {
    return view('support');
});
Route::get('/login', function () {
    return view('auth.login');
});

Route::get('/forgot-password', function () {
    return view('auth.forgot-password');
});
Route::get('/new-page', function () {
    return view('new-page');
});

Route::get('/cart', function () {
    return view('cart');
});

Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware('auth');

// Hiển thị form đăng ký
Route::get('/register', [RegisterController::class, 'showRegistrationForm'])->name('register');

// Xử lý đăng ký
Route::post('/register', [RegisterController::class, 'register']);

Route::post('/logout', [RegisterController::class, 'logout'])->name('logout');