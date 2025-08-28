<?php
use App\Http\Controllers\Auth\RegisterController;
use App\Http\Controllers\Auth\LoginController;


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

Route::get('/login', function () {
    return view('auth.login'); // Hiển thị form đăng nhập
})->name('login');

Route::post('/login', [LoginController::class, 'login'])->name('login'); // Xử lý đăng nhập

//admin routes
use Illuminate\Support\Facades\Route;

Route::prefix('admin')->group(function () {
    Route::get('/dashboard', function () {
        return view('admin.dashboard');
    })->name('admin.dashboard');

    Route::get('/products', function () {
        return view('admin.products');
    })->name('admin.products');

    Route::get('/orders', function () {
        return view('admin.orders');
    })->name('admin.orders');

    Route::get('/users', function () {
        return view('admin.users');
    })->name('admin.users');

    Route::get('/analytics', function () {
        return view('admin.analytics');
    })->name('admin.analytics');

    Route::get('/settings', function () {
        return view('admin.settings');
    })->name('admin.settings');
});