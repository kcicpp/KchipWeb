<?php

namespace App\Http\Controllers\Auth;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;

class RegisterController
{
    public function showRegistrationForm()
    {
        return view('auth.register'); // Hiển thị giao diện đăng ký
    }


public function register(Request $request)
{
    // Validate dữ liệu đầu vào
    $request->validate([
        'name' => 'required|string|max:255|unique:users', // Tên đăng nhập không được trùng
        'email' => 'required|string|email|max:255|unique:users', // Email không được trùng
        'password' => [
            'required',
            'string',
            'min:8', // Ít nhất 8 ký tự
            'regex:/[A-Z]/', // Ít nhất một chữ hoa
            'regex:/[a-z]/', // Ít nhất một chữ thường
            'regex:/[0-9]/', // Ít nhất một số
            'regex:/[^a-zA-Z0-9]/', // Ít nhất một ký tự không phải chữ cái hoặc số
            'confirmed', // Phải khớp với trường xác nhận mật khẩu
        ],
    ], [
        // Thông báo lỗi tùy chỉnh
        'name.required' => 'Tên đăng nhập là bắt buộc.',
        'name.unique' => 'Tên đăng nhập đã tồn tại.',
        'email.required' => 'Email là bắt buộc.',
        'email.email' => 'Email không hợp lệ.',
        'email.unique' => 'Email đã tồn tại.',
        'password.required' => 'Mật khẩu là bắt buộc.',
        'password.min' => 'Mật khẩu phải có ít nhất 8 ký tự.',
        'password.regex' => 'Mật khẩu phải chứa ít nhất một chữ hoa, một chữ thường, một số và một ký tự đặc biệt.',
        'password.confirmed' => 'Mật khẩu xác nhận không khớp.',
    ]);

    // Tạo tài khoản mới với ảnh đại diện mặc định
    $user = User::create([
        'name' => $request->name,
        'email' => $request->email,
        'password' => Hash::make($request->password), // Mã hóa mật khẩu
        'avatar' => '/img/default-avatar.png', // Đường dẫn ảnh đại diện mặc định
    ]);

    // Đăng nhập sau khi đăng ký
    \Illuminate\Support\Facades\Auth::login($user);

    // Chuyển hướng đến trang Home
    return redirect('/home');
}

    public function logout(Request $request)
    {
        \Illuminate\Support\Facades\Auth::logout(); // Đăng xuất người dùng

        // Xóa session và tạo lại token CSRF
        $request->session()->invalidate();
        $request->session()->regenerateToken();

        // Chuyển hướng về trang đăng nhập
        return redirect('/login');
    }
}